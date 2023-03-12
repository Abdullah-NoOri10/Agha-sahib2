from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.

# class Seller(models.Model):


class Companie(models.Model):
    name = models.CharField(max_length=220)
    location = CountryField()
    active = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=69)
    marketer = models.ForeignKey(User, on_delete=models.CASCADE)
    distributor = models.ForeignKey(Companie, on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default='29.99')

    CTAGRY_CHOICES = (
        ('dairies', 'Dairies'),
        ('vegetables', 'Vegetables'),
        ('meat', 'Meat'),
        ('fruits', 'Fruits'),
        ('packaged', 'Packaged Food'),
        ('beverages', 'Beverages'),
        ('snacks', 'Snacks'),
        ('household items', 'Household items'),
    )

    category = models.CharField(
        max_length=20, choices=CTAGRY_CHOICES, default=None)

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)
