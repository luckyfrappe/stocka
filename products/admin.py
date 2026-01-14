from django.contrib import admin
from django.utils.html import format_html
from .models import Product, AttributeType, AttributeValue, ProductAttribute, ProductImage

# Admin view was written by me and improved by Gemini AI by Google

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('thumbnail',)

    def thumbnail(self, instance):
        if instance.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', instance.image.url)
        return ""

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1
    autocomplete_fields = ['attribute_value']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'thumbnail', 'name', 'retail_price', 'price_per_week', 'time_created')
    list_filter = ('is_rentable', 'time_created')
    search_fields = ('sku', 'name', 'description')
    ordering = ('-time_created',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('sku', 'name', 'description')
        }),
        ('Pricing & Status', {
            'fields': (('retail_price', 'price_per_week'), ('is_rentable', 'has_preowned_option'))
        }),
        ('Meta Data', {
            'fields': ('time_created', 'has_sizes'),
            'classes': ('collapse',),
        }),
    )

    inlines = [ProductImageInline, ProductAttributeInline]

    def thumbnail(self, obj):
        primary_img = obj.images.filter(is_primary=True).first() or obj.images.first()
        if primary_img and primary_img.image:
            return format_html('<img src="{}" style="width: 40px; height: 40px; object-fit: cover; border-radius: 4px;" />', primary_img.image.url)
        return "No Image"
    thumbnail.short_description = 'Img'

@admin.register(AttributeType)
class AttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('attribute_type', 'value', 'slug')
    list_filter = ('attribute_type',)
    search_fields = ('value',)
    prepopulated_fields = {'slug': ('value',)}
    search_fields = ['value']