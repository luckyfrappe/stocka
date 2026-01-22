from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from .models import AttributeValue, Product, ProductAttribute, ProductImage, AttributeType
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.prefetch_related(
        'attributes__attribute_value__attribute_type'
    ).all()

    query = None
    attribute_type = None
    sort = None
    direction = None

    if request.GET:
        if 'new_arrivals' in request.GET:
            new_arrival_ids = products.order_by('-time_created').values_list('id', flat=True)[:100]
            products = products.filter(id__in=list(new_arrival_ids))

        # Debugged with help from Gemini (AI tool)
        ignore_list = ['q', 'sort', 'direction', 'page', 'new_arrivals']

        for f_type, attr_values in request.GET.lists():
            if f_type == 'attribute_type':
                products = products.filter(attributes__attribute_value__slug__in=attr_values).distinct()
                attribute_type = AttributeValue.objects.filter(slug__in=attr_values)
            elif f_type not in ignore_list:
                products = products.filter(
                    attributes__attribute_value__attribute_type__slug=f_type,
                    attributes__attribute_value__slug__in=attr_values
                ).distinct()


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'price':
                sortkey = 'retail_price'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                    
            products = products.order_by(sortkey)

    all_attribute_types = AttributeType.objects.prefetch_related('values').all()

    current_sorting = f'{sort}_{direction}'

    paginator = Paginator(products, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj, 
        'search_term': query,
        'current_attributes': attribute_type,
        'current_sorting': current_sorting,
        'all_attribute_types': all_attribute_types,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, "products/product_detail.html", context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                messages.success(request, 'Successfully added product!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to add product. Please ensure the form is valid.')
        else:
            form = ProductForm()
            
        template = 'products/add_product.html'
        context = {
            'form': form,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'Sorry, only store owners can add products.')
        return redirect(reverse('home'))


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated product!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to update product. Please ensure the form is valid.')
        else:
            form = ProductForm(instance=product)
            messages.info(request, f'You are editing {product.name}')

        template = 'products/edit_product.html'
        context = {
            'form': form,
            'product': product,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'Sorry, only store owners can edit products.')
        return redirect(reverse('home'))


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))
    else:
        messages.error(request, 'Sorry, only store owners can delete products.')
        return redirect(reverse('home'))
