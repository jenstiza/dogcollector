from random import choices
from secrets import choice
from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)
RATING = (
    ('1', '1 Star'),
    ('2', '2 Star'),
    ('3', '3 Star'),
    ('4', '4 Star'),
    ('5', '5 Star'),
)

class Toy(models.Model):
    name = models.CharField(max_length=25)
    rating = models.CharField(
        max_length=1,
        choices=RATING,
        default=RATING[4][0]
        )
    def __str__(self):
        return f'{self.get_rating_display()} for {self.name}'
    
    def get_absolute_url(self):
        return reverse("toys_detail", kwargs={'pk': self.id})
    

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    age = models.PositiveIntegerField()
    toys = models.ManyToManyField(Toy)
    
    def __str__(self):
        return f'Hi! My name is {self.name}  ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={"dog_id": self.id})
    
    
    
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
class Meta:
    ordering = ['-date']   