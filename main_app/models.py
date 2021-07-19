from django.db import models
# from django.db.models.aggregates import Max
from django.urls import reverse

class Game(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    platforms = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    price = models.IntegerField()
    release = models.DateField()

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'pk': self.id})

# Create your models here.
class Console(models.Model):
    make = models.CharField(max_length=100)
    consolemodel = models.CharField(max_length=100)
    price = models.IntegerField()
    released_year = models.IntegerField()
    # the below games need to match the views.py console_detail games
    games = models.ManyToManyField(Game)

    def __str__(self):
        return self.consolemodel

    def get_absolute_url(self):
        # the below 'console_id' is referring to urls.py detail path
        return reverse('detail', kwargs={'console_id': self.id})

class Accessory(models.Model):
    manufacture = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.IntegerField()

    # the below codes are for assigning a FOREIGNKEY to the console model, it create
    # a console_id FK. The first argument in the parameter Console is referring 
    # to the console model. The second argument on_delete=models.CASCADE is to
    # unsure that is a Console is deleted, all the child accessories will be
    # deleted automatically as well, avoiding orphan records
    # adding the below codes will also result in the admin page, when you add 
    # accessory, it will have the option for the you choose which console is
    # this accessory is for
    console = models.ForeignKey(Console, on_delete=models.CASCADE)

    def __str__(self):
        # get_type_display is a build in Django method, the middle variable can
        # be named anything, in this case type because we name it type above 
        return self.type
    
    # class Meta:
    #     ordering = ['-price']




