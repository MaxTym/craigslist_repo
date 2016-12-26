from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
    CONDITION_CHOICES = (
        ('N', 'New'),
        ('G', 'Good condition'),
        ('F', 'Fair condition')
    )
    CITY_CHOICES = (
        ('D', 'Durham'),
        ('R', 'Raleigh'),
        ('CH', 'Chapel Hill'),
        ('C', 'Carrboro'),
        ('H', 'Hillsboro'),
        ('M', 'Morrisville')
    )

    item = models.CharField(max_length=140)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)
    picture = models.FileField(upload_to='uploads/', blank=True)
    location = models.CharField(max_length=20, choices=CITY_CHOICES, blank=True)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='N')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(User)
    department = models.CharField(max_length=35, default=None)

    def __str__(self):
        return (self.item, self.price, self.description, self.picture, self.created_at, self.updated_at,)


class Profile(models.Model):
    CITY_CHOICES = (
        ('D', 'Durham'),
        ('R', 'Raleigh'),
        ('CH', 'Chapel Hill'),
        ('C', 'Carrboro'),
        ('H', 'Hillsboro'),
        ('M', 'Morrisville')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=CITY_CHOICES, default='D')

    def __str__(self):
          return self.user.username
