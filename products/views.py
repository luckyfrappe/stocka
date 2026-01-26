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
    sort = None
    direction = None
    active_filter_slugs = []
    attribute_type = None

    if request.GET:
        # Debugged with help from Gemini (AI tool)
        if 'new_arrivals' in request.GET:
            new_arrival_ids = products.order_by('-time_created').values_list('id', flat=True).distinct()[:100]
            products = products.filter(id__in=list(new_arrival_ids))

        if 'q' in request.GET:
            query = request.GET['q']
            if not query.strip():
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        ignore_list = ['q', 'sort', 'direction', 'page', 'new_arrivals']
        for key, values in request.GET.lists():
            if key not in ignore_list:
                active_filter_slugs.extend(values)
                # Filter products by the specific attribute values
                products = products.filter(attributes__attribute_value__slug__in=values)

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

    if active_filter_slugs:
        attribute_type = AttributeValue.objects.filter(slug__in=active_filter_slugs)

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
        'active_filter_slugs': active_filter_slugs,
    }

    return render(request, "products/products.html", context)

# Debugged with help from Gemini (AI tool)
def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    tags = product.attributes.select_related('attribute_value', 'attribute_value__attribute_type').all()
    
    # 1. Get the actual real size from DB (Assuming one per product)
    real_size_obj = tags.filter(attribute_value__attribute_type__name__iexact='size').first()
    real_size = real_size_obj.attribute_value.value if real_size_obj else None
    
    # 2. Define full ranges
    # Note: Ensure these match slug format or display format as needed
    CLOTHING_RANGE = ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL', '5XL']
    SHOE_RANGE = ['36', '37', '38', '39', '40', '41']
    
    simulated_sizes = []

    # 3. Determine which range to simulate based on the real size
    if real_size:
        check_val = real_size.upper()
        
        if check_val in CLOTHING_RANGE:
            simulated_sizes = CLOTHING_RANGE
        elif check_val in SHOE_RANGE or check_val.isdigit():
            simulated_sizes = SHOE_RANGE
        elif 'ONESIZE' in check_val:
            simulated_sizes = ['Onesize']
        else:
            # Fallback if it's a weird size not in the lists
            simulated_sizes = [real_size]
    else:
        # Default fallback if no size attribute exists
        simulated_sizes = ['Onesize']

    # Get other tags for display
    product_tags = {}
    for tag in tags:
        attr_type = tag.attribute_value.attribute_type.name
        if attr_type not in product_tags:
            product_tags[attr_type] = []
        product_tags[attr_type].append(tag.attribute_value)

    context = {
        'product': product,
        'product_tags': product_tags,
        'simulated_sizes': simulated_sizes, # For Buy New / Rent
        'real_size': real_size,             # For Pre-Owned
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

# AI tools were used to assist with the initial implementation. I reviewed and adapted the code to fit the project.
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
def delete_image(request, image_id):
    """ Delete a specific product image """
    if request.user.is_superuser:
        image = get_object_or_404(ProductImage, pk=image_id)
        product_id = image.product.id
        image.delete()
        messages.success(request, 'Image removed from gallery.')
        
        return redirect(reverse('edit_product', args=[product_id]))
    else:
        messages.error(request, 'Sorry, only store owners can delete product images.')
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
