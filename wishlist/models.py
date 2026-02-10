from django.db import models


class Wishlist(models.Model):
    """
    Represents a collection of products saved by a user for future consideration.

    model: `User` (OneToOneField), `Product` (ManyToManyField)
    """
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Product', blank=True)

    def __str__(self):
        """
        Returns a string representation of the wishlist belonging to the user.
        """
        return f"{self.user.username}'s Wishlist"
