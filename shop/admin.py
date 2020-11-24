from django.contrib import admin
from .models import Shop
# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'user', 'industry', 'business_start',
                'franchise_start', 'headquarter', 'units',
                'description']
    prepopulated_fields = {'slug' : ('name',)}