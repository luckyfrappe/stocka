from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from products.models import Product


@login_required
def view_wishlist(request):
    """ A view to redirect to all_products filtered by wishlist items """
    wishlist = Wishlist.objects.filter(user=request.user).first()
    redirect_url = request.META.get('HTTP_REFERER', reverse('products'))

    # If the wishlist doesn't exist OR has no products
    if not wishlist or not wishlist.products.exists():
        messages.info(request, "Your wishlist is empty.")
        return redirect(redirect_url)

    # Get the list of product IDs
    wishlist_ids = list(wishlist.products.values_list('id', flat=True))

    ids_string = ",".join(map(str, wishlist_ids))

    return redirect(f"{reverse('products')}?wishlist_items={ids_string}")


@login_required
def add_to_wishlist(request, product_id):
    """ Add a product to the user's wishlist """
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    redirect_url = request.META.get('HTTP_REFERER', reverse('products'))

    if product in wishlist.products.all():
        messages.info(request, "This product is already in your wishlist.")
    else:
        wishlist.products.add(product)
        messages.success(
            request,
            f"{product.name} has been added to your wishlist."
        )

    return redirect(redirect_url)


@login_required
def remove_from_wishlist(request, product_id):
    """ Remove a product from the user's wishlist """
    wishlist = Wishlist.objects.filter(user=request.user).first()
    redirect_url = request.META.get('HTTP_REFERER', reverse('products'))

    if not wishlist:
        messages.error(
            request,
            "You don't have a wishlist to remove items from."
        )
        return redirect(redirect_url)

    product = get_object_or_404(Product, id=product_id)

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(
            request,
            f"{product.name} has been removed from your wishlist."
        )
    else:
        messages.info(request, "This product is not in your wishlist.")

    return redirect(redirect_url)
