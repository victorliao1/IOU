from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class moneyowed(models.Model):
    amount = models.IntegerField()
    person = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def publish(self):
        self.save()
    
class CustomUser(AbstractUser):
    
    def __str__(self):
        return self.email
