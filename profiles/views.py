from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from checkout.models import Order
from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    """
    Displays the user's profile and handles updates to delivery information.

    model: `UserProfile`, `Order`
    form: `UserProfileForm`

    **context**:
    - `form`: instance of `UserProfileForm` populated with user data
    - `orders`: QuerySet of confirmed orders related to the user profile
    - `on_profile_page`: boolean used to toggle specific UI elements

    template: `profiles/profile.html`
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.filter(payment_confirmed=True).order_by('-date')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Displays a summary of a past order confirmation.

    model: `Order`

    **context**:
    - `order`: single instance of model `Order`
    - `from_profile`: boolean indicating the view was accessed via the profile

    template: `checkout/checkout_success.html`
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
