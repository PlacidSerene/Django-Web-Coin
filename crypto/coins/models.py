from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.FloatField(default=500)
    at_date = models.DateField(auto_now_add=True)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    price = models.FloatField()
    coin_name = models.TextField()
    coin_receive = models.FloatField()
    at_time = models.TimeField(auto_now_add=True)
    at_date = models.DateField(auto_now_add=True)
    buying = models.BooleanField(default=True)

class Asset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asset')
    coin_name = models.TextField()
    coin_amount = models.FloatField()

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history')
    at_date = models.DateField(auto_now_add=True)
    total = models.FloatField()