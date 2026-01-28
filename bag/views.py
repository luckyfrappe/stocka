from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

# The views below were assisted by Gemini AI tool and modified by the author to fit project needs.
def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    purchase_type = request.POST.get('purchase_type', 'new')
    rental_period = int(request.POST.get('rental_period', 1))
    size = request.POST.get('product_size', 'OS') # Default to One Size
    
    bag = request.session.get('bag', {})
    
    if item_id not in bag:
        bag[item_id] = {'items_by_size': {}}
    
    item_key = f"{size}_{purchase_type}"

    if item_key in bag[item_id]['items_by_size']:
        bag[item_id]['items_by_size'][item_key]['quantity'] += quantity
        messages.success(request, f'Updated {product.name} ({size.upper()}) ({purchase_type.upper()}) quantity to {bag[item_id]["items_by_size"][item_key]["quantity"]} in your bag')
    else:
        bag[item_id]['items_by_size'][item_key] = {
            'quantity': quantity,
            'type': purchase_type,
            'rental_period': rental_period,
            'size': size
        }
        messages.success(request, f'Added {quantity} x {product.name} ({size.upper()}) ({purchase_type.upper()}) to your bag')

    
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    item_key = request.POST.get('item_key') # Received from hidden input
    bag = request.session.get('bag', {})

    if item_id in bag and item_key in bag[item_id]['items_by_size']:
        item_info = bag[item_id]['items_by_size'][item_key]
        
        if quantity > 0:
            bag[item_id]['items_by_size'][item_key]['quantity'] = quantity
            messages.success(request, f'Updated ({item_info["size"].upper()}) ({item_info["type"].upper()}) {product.name} quantity to {quantity}')
        else:
            del bag[item_id]['items_by_size'][item_key]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed ({item_info["size"].upper()}) ({item_info["type"].upper()}) {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
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
            messages.success(request, f'Removed ({size.upper()}) ({p_type.upper()}) {product.name} from your bag')
            return HttpResponse(status=200)
        return HttpResponse(status=404)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)