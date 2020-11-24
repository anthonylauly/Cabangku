from django.contrib import admin
from .models import TransactionModels

# Register your models here.
@admin.register(TransactionModels)
class TransactionAdmin(admin.ModelAdmin):
    fields = [field.name for field in TransactionModels._meta.get_fields()]
    readonly_fields = ['transaction_date', 'id']
