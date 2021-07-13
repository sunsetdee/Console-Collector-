from django.db import models

# Create your models here.
class Console():
    def __init__(self, make, model, released_year, price):
        self.make = make
        self.model = model
        self.released_year = released_year
        self.price = price

consoles = [
    Console('Microsoft', 'Xbox Serie X', 2020, '$499'),
    Console('Microsoft', 'Xbox One', 2013, '$499'),
    Console('Sony', 'PlayStation 5', 2020, '$499'),
    Console('Sony', 'PlayStation 4', 2013, '$399'),
    Console('Nintendo', 'Switch', 2017, '$299'),
]
