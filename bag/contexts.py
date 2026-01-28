from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
# This context processor was simplified and modified with help from Gemini AI tool to fit project needs.
def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        
        if isinstance(item_data, dict) and 'items_by_size' in item_data:
            for item_key, info in item_data['items_by_size'].items():
                quantity = info['quantity']
                p_type = info['type']
                weeks = info.get('rental_period', 1)

                # Determine Price based on Business Logic
                if p_type == 'rent':
                    price = product.price_per_week * weeks
                elif p_type == 'preowned':
                    price = round(float(product.retail_price) * 0.60, 2) # 40% off for Pre-owned
                else:
                    price = product.retail_price

                total += quantity * price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'item_key': item_key,
                    'quantity': info['quantity'],
                    'product': product,
                    'size': info.get('size', 'OS'),
                    'purchase_type': info.get('type', 'new'),
                    'rental_period': info.get('rental_period', 1),
                    'price_each': price,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context