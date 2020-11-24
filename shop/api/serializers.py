from rest_framework import serializers

from django.utils.text import slugify

from ..models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields= '__all__'