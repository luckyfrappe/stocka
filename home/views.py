from django.shortcuts import render
from products.models import AttributeValue, Product, ProductImage


def index(request):
    """
    Displays the homepage.

    model: `AttributeValue` - brands

    **context**
    - `brands`: brands to show on homepage

    template: `home/index.html`
    """
    brands = AttributeValue.objects.filter(
        attribute_type__name__iexact='Brand'
    ).order_by('?')[:20]

    context = {
        'brands': brands,
    }
    return render(request, 'home/index.html', context)