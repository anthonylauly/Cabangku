from rest_framework import serializers

from ..models import TransactionModels

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionModels
        fields = '__all__'