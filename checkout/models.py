import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from decimal import Decimal

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class PurchaseType(models.TextChoices):
    NEW = 'new', 'New'
    RENT = 'rent', 'Rent'
    PREOWNED = 'preowned', 'Preowned'
    BUYOUT = 'buyout', 'Buyout'
    EXTEND = 'extend', 'Extend'


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True) # XS, S, M, L, XL
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank=False, editable=False)
    purchase_type = models.CharField(
        max_length=10, 
        choices=PurchaseType.choices
    )
    rental_period = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Calculates line item total based on purchase type and quantity.
        """
        # 1. Logic for Rentals and Extensions
        if self.purchase_type in [PurchaseType.RENT, PurchaseType.EXTEND]:
            period = self.rental_period or 1
            base_price = self.product.price_per_week * period
        
        # 2. Logic for Preowned (using settings rate)
        elif self.purchase_type == PurchaseType.PREOWNED:
            discount = Decimal(str(settings.PREOWNED_DISCOUNT_RATE))
            base_price = (self.product.retail_price * discount).quantize(Decimal('0.00'))

        # 3. Logic for Buyout
        elif self.purchase_type == PurchaseType.BUYOUT:
            period = self.rental_period or 1
            buyout_discount = Decimal(str(settings.BUYOUT_DISCOUNT_RATE))
            rental_cost = self.product.price_per_week * period
            discounted_price = (self.product.retail_price * buyout_discount).quantize(Decimal('0.00'))
            base_price = rental_cost + discounted_price
        
        # 4. Logic for New
        else:
            base_price = self.product.retail_price

        self.lineitem_total = base_price * self.quantity
        super().save(*args, **kwargs)
