from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriptions_list, name='subscriptions'),
    path('mark_as_returned/<int:subscription_id>/', views.mark_as_returned, name='mark_as_returned'),
]
