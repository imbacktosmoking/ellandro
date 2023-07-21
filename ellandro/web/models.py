from django.db import models
from django.utils import timezone

# Create your models here.

class Client(models.Model):
    author = models.CharField(max_length=254) 
    email = models.EmailField(max_length=254)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now) 

