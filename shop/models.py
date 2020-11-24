from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

import datetime
import os
from io import StringIO
from PIL import Image

# Create your models here.
def rename_and_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.user.id, instance.slug, ext)
    return os.path.join('shop_logo/', filename)

class IntegerBoundedField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerBoundedField, self).formfield(**defaults)

class Shop(models.Model):
    industry_choice = [
        ('aerospace', 'Aerospace Industry'),
        ('transport', 'Transport Industry'),
        ('computer', 'Computer Industry'),
        ('telecommunication', 'Telecommunication Industry'),
        ('agriculture', 'Agriculture Industry'),
        ('construction', 'Construction Industry'),
        ('education', 'Education Industry'),
        ('pharmaceutical', 'Pharmaceutical Industry'),
        ('food', 'Food Industry'),
        ('health', 'Health Care Industry'),
        ('hospitality', 'Hospitality Industry'),
        ('entertainment', 'Entertainment Industry'),
        ('news_media', 'News Media Industry'),
        ('energy', 'Energy Industry'),
        ('manufacturing', 'Manufacturing Industry'),
        ('music', 'Music Industry'),
        ('mining', 'Mining Industry'),
        ('web', 'Worldwide Web'),
        ('electronic', 'Electronics Industry'),

    ]
    date = datetime.datetime.now()
    year_now = int(date.strftime('%Y'))

    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                related_name='owner')
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(default='')
    logo = models.ImageField(upload_to=rename_and_path)
    industry = models.CharField(max_length= 20, choices=industry_choice)
    business_start = IntegerBoundedField(min_value=1950, max_value=year_now)
    franchise_start = IntegerBoundedField(min_value=1950, max_value=year_now)
    headquarter = models.CharField(max_length=100)
    units = models.IntegerField()
    description = models.TextField()
    joined = models.DateTimeField(auto_now_add=True)
    tenant = models.ManyToManyField(User, blank=True, 
                related_name='tenant')
    is_active = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.get_industry_display())

