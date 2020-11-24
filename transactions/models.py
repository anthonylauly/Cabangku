from django.db import models
from django.contrib.auth.models import User

from shop.models import Shop

# Create your models here.
class TransactionModels(models.Model):
    shop = models.ForeignKey(Shop, null=True, on_delete=models.SET_NULL)
    buyer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    has_paid = models.BooleanField(default=False)
    final_price = models.PositiveIntegerField()
    contract_length = models.PositiveIntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    paid_date = models.DateTimeField(default=None, null=True)