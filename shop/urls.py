from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_list, name='shop_list'),
    path('shop_upload/', views.shop_upload, name='shop_upload'),
    path('shop_search/', views.shop_search, name='shop_search'),
]