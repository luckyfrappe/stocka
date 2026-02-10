from django.db import models


class AttributeType(models.Model):
    """
    Defines categories for product specifications.

    Used to group specific values such as 'Brand', 'Color', or 'Material'.
    """
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    """
    Stores specific values for a given AttributeType.

    model: `AttributeType`
    """
    attribute_type = models.ForeignKey(
        AttributeType,
        on_delete=models.CASCADE,
        related_name="values"
    )
    value = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        unique_together = ('attribute_type', 'value')

    def __str__(self):
        return f"{self.value}"


class Product(models.Model):
    """
    The central entity representing a stockable item in the inventory.

    model: `ProductAttribute`, `ProductImage`
    """
    sku = models.CharField(max_length=255, unique=True)  # Maps to 'id' in CSV
    name = models.CharField(max_length=255)
    description = models.TextField()
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2)
    time_created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    """
    The link table connecting Products to their specific AttributeValues.

    model: `Product`, `AttributeValue`
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="attributes"
    )
    attribute_value = models.ForeignKey(
        AttributeValue,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('product', 'attribute_value')

    def __str__(self):
        return str(self.attribute_value.value)


class ProductImage(models.Model):
    """
    Manages the visual gallery for each Product.

    model: `Product`
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='products/')
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order']
