from django.db import models


class Wishlist(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Product', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
