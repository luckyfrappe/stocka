from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
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
    
    context = {
        'subscriptions': user_subscriptions,
    }
    
    return render(request, 'subscriptions/subscriptions.html', context)

def mark_as_returned(request, product_id):
    """
    Marks a subscription as returned.
    """
    subscription = Subscriptions.objects.get(user=request.user, product__id=product_id)
    subscription.status = 'returned'
    subscription.save()
    return redirect('subscriptions_list')