from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'transactions'

router = routers.SimpleRouter()
router.register('transaction', views.TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]