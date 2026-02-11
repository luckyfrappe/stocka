from django.contrib import messages
from django.shortcuts import (
    get_object_or_404,
    HttpResponse,
    redirect,
    render,
    reverse
)
from products.models import Product


def view_bag(request):
    """
    Renders the shopping bag summary page.

    **context**:
    - Inherits global context from `bag_contents` processor.

    template: `bag/bag.html`
    """
    return render(request, 'bag/bag.html')


# The views below were assisted by Gemini AI tool
# and modified by the author to fit project needs.
def add_to_bag(request, item_id):
    """
    Adds a product variant to the session bag or updates its quantity.

    model: `Product`

    **context**:
    - `bag`: updates the session-based dictionary with item metadata
    (size, type, period)

    template: redirects to `checkout` for express items or the previous URL
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    purchase_type = request.POST.get('purchase_type', 'new')
    rental_period = int(request.POST.get('rental_period', 1))
    start_date = request.POST.get('start_date', None)
    size = request.POST.get('product_size', 'OS')  # Default to One Size

    bag = request.session.get('bag', {})

    # 1. Identify if the bag currently has an express Item (Buyout/Extend)
    has_express_in_bag = any(
        info.get('type') in ['buyout', 'extend']
        for item in bag.values()
        for info in item.get('items_by_size', {}).values()
    )

    # 2. Safety Logic
    if purchase_type in ['buyout', 'extend']:
        # Wipe the bag if adding a new express item.
        bag = {}
        redirect_url = reverse('checkout')
    elif has_express_in_bag:
        # If user has an express item and try to add a normal product:
        messages.info(
            request,
            "Please complete your current transaction "
            "or remove the item before adding new items."
        )
        return redirect(reverse('view_bag'))
    else:
        # Standard behavior for normal products
        redirect_url = request.POST.get('redirect_url')

    if item_id not in bag:
        bag[item_id] = {'items_by_size': {}}

    item_key = f"{size}_{purchase_type}_{rental_period}_{start_date}"

    if item_key in bag[item_id]['items_by_size']:
        bag[item_id]['items_by_size'][item_key]['quantity'] += quantity
        messages.success(
            request,
            f'Updated {product.name} ({size.upper()}) '
            f'({purchase_type.upper()}) quantity to '
            f'{bag[item_id]["items_by_size"][item_key]["quantity"]} '
            f'in your bag'
        )
    else:
        bag[item_id]['items_by_size'][item_key] = {
            'quantity': quantity,
            'type': purchase_type,
            'rental_period': rental_period,
            'size': size,
            'start_date': start_date
        }
        messages.success(
            request,
            f'Added {quantity} x {product.name} ({size.upper()}) '
            f'({purchase_type.upper()}) to your bag'
        )

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Updates the quantity of a specific item variant or removes it if quantity
    is zero.

    model: `Product`

    **context**:
    - `bag`: modifies the `item_key` entry within the session dictionary

    template: redirects to `view_bag`
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    item_key = request.POST.get('item_key')  # Received from hidden input
    bag = request.session.get('bag', {})

    if item_id in bag and item_key in bag[item_id]['items_by_size']:
        item_info = bag[item_id]['items_by_size'][item_key]

        if quantity > 0:
            bag[item_id]['items_by_size'][item_key]['quantity'] = quantity
            messages.success(
                request,
                f'Updated ({item_info["size"].upper()}) '
                f'({item_info["type"].upper()}) {product.name} '
                f'quantity to {quantity}'
            )
        else:
            del bag[item_id]['items_by_size'][item_key]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed ({item_info["size"].upper()}) '
                f'({item_info["type"].upper()}) {product.name} from your bag'
            )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Removes a specific product variant from the session bag via
    an AJAX request.

    model: `Product`

    **context**:
    - `bag`: deletes the variant key from the session dictionary

    template: returns a standard `HttpResponse` status
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        item_key = request.POST.get('item_key')
        bag = request.session.get('bag', {})
        item_info = bag[item_id]['items_by_size'].get(item_key, {})
        size = item_info.get('size', 'OS')
        p_type = item_info.get('type', '')

        if item_id in bag and item_key in bag[item_id]['items_by_size']:
            del bag[item_id]['items_by_size'][item_key]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)

            request.session['bag'] = bag
            messages.success(
                request,
                f'Removed ({size.upper()}) ({p_type.upper()}) '
                f'{product.name} from your bag'
            )
            return HttpResponse(status=200)
        return HttpResponse(status=404)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
