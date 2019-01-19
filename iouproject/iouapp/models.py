from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class MoneyOwed(models.Model):
    owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    amount = models.IntegerField()
    toPerson = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def publish(self):
        self.save()


class CustomUser(AbstractUser):
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email
