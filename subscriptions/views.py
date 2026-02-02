from django.shortcuts import render
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