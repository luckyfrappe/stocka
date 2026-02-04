from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Subscriptions

@login_required
def subscriptions_list(request):
    """
    Displays the user's subscription history with performance optimization.
    """
    user_subscriptions = Subscriptions.objects.filter(
        user=request.user
    ).select_related(
        'product', 
        'order_line_item__order' 
    ).order_by('-start_date')
    buyout_price = None
    for sub in user_subscriptions:
        price_per_week = sub.product.price_per_week
        sub.price_per_week = price_per_week
        if sub.status == 'active':
            sunk_cost = sub.product.price_per_week * sub.duration_weeks
            buyout_price = sub.product.retail_price - sunk_cost
            sub.buyout_price = max(buyout_price, 0)
    
    context = {
        'subscriptions': user_subscriptions,
    }
    
    return render(request, 'subscriptions/subscriptions.html', context)

def mark_as_returned(request, subscription_id):
    """
    Marks a subscription as returned.
    """
    subscriptions = get_object_or_404(Subscriptions, id=subscription_id, user=request.user)
    subscriptions.status = 'returned'
    subscriptions.save()
    return redirect('subscriptions')