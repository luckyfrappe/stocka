from django.contrib import admin
from django.utils.html import format_html
from .models import (
    AttributeType,
    AttributeValue,
    Product,
    ProductAttribute,
    ProductImage
)


# Admin view was written by me and improved by Gemini AI by Google
class ProductImageInline(admin.TabularInline):
    """
    Inline gallery management for product images.

    model: `ProductImage`
    """
    model = ProductImage
    extra = 1
    readonly_fields = ('thumbnail',)

    def thumbnail(self, instance):
        """
        Displays a small image preview within the inline admin rows.
        """
        if instance.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: auto;" />',
                instance.image.url
            )
        return ""


# ProductAttributeInline was written by Gemini AI by Google
class ProductAttributeInline(admin.TabularInline):
    """
    Inline management for product specifications using the EAV model.

    model: `ProductAttribute`
    """
    model = ProductAttribute
    extra = 1
    autocomplete_fields = ['attribute_value']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Primary interface for managing the product catalog and inventory.

    model: `Product`

    **fields**:
    - `list_display`: summary of product identity, pricing, and visuals
    - `fieldsets`: grouped layout for commercial and metadata organization
    """
    list_display = (
        'sku',
        'thumbnail',
        'name',
        'retail_price',
        'price_per_week',
        'time_created'
    )
    list_filter = ('time_created',)
    search_fields = ('sku', 'name', 'description')
    ordering = ('-time_created',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('sku', 'name', 'description')
        }),
        ('Pricing', {
            'fields': (('retail_price', 'price_per_week'),)
        }),
        ('Meta Data', {
            'fields': ('time_created',),
            'classes': ('collapse',),
        }),
    )

    inlines = [ProductImageInline, ProductAttributeInline]

    def thumbnail(self, obj):
        """
        Returns a formatted HTML thumbnail for the product list view.
        """
        primary_img = obj.images.first()
        if primary_img and primary_img.image:
            return format_html(
                '<img src="{}" style="width: 40px; height: 40px; '
                'object-fit: cover; border-radius: 4px;" />',
                primary_img.image.url
            )
        return "No Image"
    thumbnail.short_description = 'Img'


@admin.register(AttributeType)
class AttributeTypeAdmin(admin.ModelAdmin):
    """
    Interface for defining global specification categories.

    model: `AttributeType`
    """
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    """
    Interface for managing individual values within attribute types.

    model: `AttributeValue`
    """
    list_display = ('attribute_type', 'value', 'slug')
    list_filter = ('attribute_type',)
    search_fields = ('value',)
    prepopulated_fields = {'slug': ('value',)}
    search_fields = ['value']
