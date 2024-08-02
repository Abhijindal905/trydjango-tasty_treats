from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()
class car(models.Model):
    car_name = models.CharField(max_length=123)
    car_speed = models.IntegerField(default=50)

def __str__(self):
    return self.car_name
