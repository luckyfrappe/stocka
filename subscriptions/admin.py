from django.contrib import admin
from .models import Subscriptions

# Register your models here.
@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'start_date', 'end_date', 'status')
    search_fields = ('user__username', 'product__name')
    list_filter = ('status', 'start_date', 'end_date')