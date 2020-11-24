from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'shop'

router = routers.SimpleRouter()
router.register('shop', views.ShopViewSet)

urlpatterns = [
        path('', include(router.urls)),
]