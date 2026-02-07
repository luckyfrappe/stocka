from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Case, When, Value, IntegerField
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
    ).annotate(
        # Assign a numerical priority to statuses, created by Gemini AI tool
        priority=Case(
            When(status='overdue', then=Value(1)),
            When(status='active', then=Value(2)),
            default=Value(3),
            output_field=IntegerField(),
        )
    ).order_by('priority', '-start_date')

    paginator = Paginator(user_subscriptions, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    buyout_price = None
    for sub in page_obj:
        price_per_week = sub.product.price_per_week
        sub.price_per_week = price_per_week
        if sub.status == 'active':
            sunk_cost = sub.product.price_per_week * sub.duration_weeks
            buyout_price = sub.product.retail_price - sunk_cost
            sub.buyout_price = max(buyout_price, 0)
    
    context = {
        'subscriptions': page_obj,
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

def mark_as_bought_out(request, subscription_id):
    """
    Marks a subscription as bought out if buy out is price is 0. Checks the buyout price on backend to prevent any manipulation from the frontend. If buyout price is above 0, redirects to subscriptions page without making any changes.
    """
    subscriptions = get_object_or_404(Subscriptions, id=subscription_id, user=request.user)
    price_per_week = subscriptions.product.price_per_week
    sunk_cost = price_per_week * subscriptions.duration_weeks
    buyout_price = subscriptions.product.retail_price - sunk_cost
    
    if buyout_price <= 0:
        subscriptions.status = 'bought_out'
        subscriptions.save()
        messages.success(request, f'You have successfully bought out {subscriptions.product.name}. It is now yours to keep!')
    else:
        messages.error(request, f'We encountered an issue with your request to buy out {subscriptions.product.name}. Please contact support for assistance.')
    
    return redirect('subscriptions')
