from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'profile'

router = routers.SimpleRouter()
router.register('profile', views.ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]