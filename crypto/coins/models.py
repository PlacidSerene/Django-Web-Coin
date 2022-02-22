from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fund = models.IntegerField(default=500)

    