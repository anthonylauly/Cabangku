from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(User):
    phone_number = PhoneNumberField()
    birthdate = models.DateField()
    gender = models.CharField(max_length=6)
