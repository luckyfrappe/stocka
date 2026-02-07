from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('info/<str:page_name>/', views.info_pages, name='info_pages'),
]
