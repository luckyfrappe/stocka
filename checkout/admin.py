from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Provides an inline interface for OrderLineItems within the Order
    admin page.

    model: `OrderLineItem`
    Sets `lineitem_total` to read-only to prevent manual override
    of calculated prices.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Order model.

    Displays customer information, order totals, and payment status.
    Includes `OrderLineItemAdminInline` to manage individual products
    within an order.

    model: `Order`
    **Fields**:
    - `readonly_fields`: Protects financial and system-generated data
    (totals, dates, PIDs).
    - `list_display`: Provides a summary view of orders for
    quick business reporting.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid',)

    fields = ('order_number', 'userprofile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city',
              'street_address1', 'street_address2',
              'county', 'delivery_cost', 'order_total',
              'grand_total', 'original_bag',
              'stripe_pid', 'payment_confirmed',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total', 'payment_confirmed',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
