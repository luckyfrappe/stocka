from django.db import models
from django.utils.text import slugify

class AttributeType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class AttributeValue(models.Model):
    attribute_type = models.ForeignKey(AttributeType, on_delete=models.CASCADE, related_name="values")
    value = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        unique_together = ('attribute_type', 'value')

    def __str__(self):
        return f"{self.attribute_type.name}: {self.value}"

class Product(models.Model):
    sku = models.CharField(max_length=255, unique=True) # Maps to 'id' in CSV
    name = models.CharField(max_length=255)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2)
    is_rentable = models.BooleanField(default=True)
    has_preowned_option = models.BooleanField(default=False)
    time_created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="attributes")
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'attribute_value')

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order']
    