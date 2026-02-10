from django.conf import settings
from django.db import models
from django.utils import timezone


class SubscriptionStatus(models.TextChoices):
    """
    Defines the possible states of a subscription lifecycle.
    """
    ACTIVE = 'active', 'Active'
    RETURNED = 'returned', 'Returned'
    BOUGHT_OUT = 'bought_out', 'Bought Out'
    OVERDUE = 'overdue', 'Overdue'
    CANCELLED = 'cancelled', 'Cancelled'


class Subscriptions(models.Model):
    """
    Tracks product rentals and lifecycle status for individual users.

    model: `User`, `Product`, `OrderLineItem`
    Links a user to a specific product through their checkout line item.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='subscriptions'
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.PROTECT
    )
    order_line_item = models.OneToOneField(
        'checkout.OrderLineItem',
        on_delete=models.PROTECT,
        related_name='subscription_record'
    )

    # Subscription Lifecycle
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    duration_weeks = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=SubscriptionStatus.choices,
        default=SubscriptionStatus.ACTIVE
    )

    class Meta:
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        """
        Returns a string representation of the subscription ID and user.
        """
        return f"Sub {self.id}: {self.user.username} - {self.product.name}"
