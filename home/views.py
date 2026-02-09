from django.shortcuts import render, Http404
from products.models import AttributeValue, Product


def index(request):
    """
    Displays the homepage.

    model: `AttributeValue` - brands
    model: `Product` - products

    **context**
    - `brands`: brands to show on homepage
    - `spring_items`: spring collection products to show on homepage
    - `everyday_items`: everyday essentials products to show on homepage

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
    """ A single view to handle all brand/legal pages with a safety check """
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
