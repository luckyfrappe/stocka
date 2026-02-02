from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta, datetime
from django.utils.dateparse import parse_date

from checkout.models import OrderLineItem, PurchaseType
from .models import Subscriptions

@receiver(post_save, sender=OrderLineItem)
def create_or_update_subscription(sender, instance, created, **kwargs):
    """
    Handles Subscription creation, extension, and buyout triggers.
    """
    if not created:
        return

    if not instance.order.userprofile:
        return 
    
    customer = instance.order.userprofile.user 
    weeks = int(instance.rental_period or 0)
    start_date = instance.start_date
    if isinstance(start_date, str):
        start_date = parse_date(start_date)
    # RENT (Create New)
    if instance.purchase_type == PurchaseType.RENT:
        
        # calculate end date
        end_date = (
            start_date + timedelta(weeks=weeks)
            if start_date and weeks
            else None
        )
        Subscriptions.objects.create(
            user=customer,
            product=instance.product,
            order_line_item=instance, # Links this specific line item to the sub
            duration_weeks=weeks,
            start_date=start_date,
            end_date=end_date,
            status='active'
        )

    # EXTEND or BUYOUT (Modify Existing)
    elif instance.purchase_type in [PurchaseType.EXTEND, PurchaseType.BUYOUT]:
        
        try:
            active_sub = Subscriptions.objects.filter(
                user=customer,
                product=instance.product,
                status='active'
            ).latest('start_date')
            
            if instance.purchase_type == PurchaseType.EXTEND:
                # Add weeks to duration
                active_sub.duration_weeks += weeks
                # Add weeks to end_date
                if active_sub.end_date:
                    active_sub.end_date += timedelta(weeks=weeks)
                active_sub.status = 'active'  # Ensure status remains active
                active_sub.save()
                
            elif instance.purchase_type == PurchaseType.BUYOUT:
                active_sub.status = 'bought_out'
                active_sub.end_date = None # Ownership is permanent now
                active_sub.save()

        except Subscriptions.DoesNotExist:
            pass  # No active subscription found; nothing to extend or buy out