from django.shortcuts import Http404, render
from products.models import AttributeValue, Product


def index(request):
    """
    Renders the primary homepage with curated product collections and
    brand partners.

    model: `AttributeValue`, `Product`

    **context**:
    - `brands`: randomized selection of brand attributes
    - `spring_items`: products tagged with the 'spring' attribute
    - `everyday_items`: products tagged with the 'everyday' attribute

    template: `home/index.html`
    """
    brands = AttributeValue.objects.filter(
        attribute_type__name__iexact='Brand'
    ).order_by('?')[:20]

    products = Product.objects.prefetch_related(
        'images', 'attributes__attribute_value'
    )

    spring_items = products.filter(
        attributes__attribute_value__slug='spring'
    ).distinct()[:4]

    everyday_items = products.filter(
        attributes__attribute_value__slug='everyday'
    ).distinct()[:4]

    context = {
        'brands': brands,
        'spring_items': spring_items,
        'everyday_items': everyday_items,
    }
    return render(request, 'home/index.html', context)


# A single view to handle all brand/legal pages
# Scallable solution providedby Gemini AI tool
def info_pages(request, page_name):
    """
    A dynamic router for brand, legal, and static information pages.

    model: `AttributeValue`

    **context**:
    - `brands`: list of brand attributes for specific marketing pages

    template: `home/{page_name}.html`
    """
    template_path = f'home/{page_name}.html'

    if page_name == 'values':
        brands = AttributeValue.objects.filter(
            attribute_type__name__iexact='Brand'
        ).order_by('?')[:20]
        context = {'brands': brands}
        return render(request, template_path, context)

    try:
        return render(request, template_path)
    except Exception:
        raise Http404("This info page does not exist.")
