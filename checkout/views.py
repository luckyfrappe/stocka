import json

from django.conf import settings
from django.contrib import messages
from django.shortcuts import (
    get_object_or_404,
    HttpResponse,
    redirect,
    render,
    reverse
)

from django.views.decorators.http import require_POST
import stripe

from .forms import OrderForm
from .models import Order, OrderLineItem
from bag.contexts import bag_contents
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile


@require_POST
def cache_checkout_data(request):
    """
    Caches checkout metadata in the Stripe PaymentIntent for data persistence.

    **context**:
    - `client_secret`: unique transaction identifier from Stripe
    - `save_info`: boolean indicating user preference for data retention
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'save_info': request.POST.get('save_info'),
            'username': str(request.user),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Processes the payment transaction and creates order and line item records.

    model: `Order`, `OrderLineItem`, `Product`, `UserProfile`
    form: `OrderForm`

    **context**:
    - `order_form`: instance of `OrderForm` for customer data entry
    - `stripe_public_key`: credential for Stripe.js integration
    - `client_secret`: key used to confirm the payment on the client side

    template: `checkout/checkout.html`
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)

            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
                order.userprofile = profile

            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if (isinstance(item_data, dict) and
                            'items_by_size' in item_data):
                        for item_key, info in (
                                item_data['items_by_size'].items()):
                            quantity = info['quantity']
                            purchase_type = info.get('type', 'new')
                            rental_period = info.get('rental_period', 1)
                            size = info.get('size', 'OS')
                            start_date_raw = info.get('start_date')

                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                                purchase_type=purchase_type,
                                rental_period=rental_period,
                                start_date=start_date_raw,
                            )
                            order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't "
                        "found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number])
            )
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request,
                "There's nothing in your bag at the moment"
            )
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Renders the order confirmation page and finalizes profile data.

    model: `Order`, `UserProfile`
    form: `UserProfileForm`

    **context**:
    - `order`: specific instance of model `Order` for display

    template: `checkout/checkout_success.html`
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.userprofile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_country': order.country,
            }
            userprofile_form = UserProfileForm(profile_data, instance=profile)
            if userprofile_form.is_valid():
                userprofile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
