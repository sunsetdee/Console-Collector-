from django.db import models
from django.urls import reverse

# Create your models here.
class Console(models.Model):
    make = models.CharField(max_length=100)
    consolemodel = models.CharField(max_length=100)
    price = models.IntegerField()
    released_year = models.IntegerField()

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('detail', kwargs={'console_id': self.id})


