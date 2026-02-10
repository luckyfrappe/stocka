from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculates the subtotal for a line item.

    **context**:
    - `price`: unit price of the product variant
    - `quantity`: number of units of the variant in the bag

    Used in bag and checkout templates to display line item totals.
    """
    return price * quantity
