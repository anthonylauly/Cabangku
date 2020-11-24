from django.urls import path, include
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.shop_list, name='shop_list'),
    path('signin/', views.shop_upload, name='shop_upload'),
    path('signup/', views.shop_search, name='shop_search'),
]