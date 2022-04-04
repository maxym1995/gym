from django.db import models

# Create your models here.
# from gym_app.models import *

SEX = (
    (0, "Female"),
    (1, "Male"),

)

TRAININGS = (
    (0, "Personal"),
    (1, "GCT"),
    (2, "Pilates"),
    (3, "Stretching"),
    (4, "K1"),
    (5, "MMA"),
    (6, "Box"),
)

TYPES = (
    (0, "Trainer"),
    (1, "Recepctionist"),
    (2, "Director"),
    (3, "Accountant"),
)

class Members(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    sex = models.IntegerField(choices=SEX)
    year_of_birth = models.IntegerField(null=True)

class Staff(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    year_of_birth = models.IntegerField(null=True)
    type = models.CharField(max_length=64, choices = TYPES)

class Trainings(models.Model):
    name = models.CharField(max_length=64, choices = TRAININGS)
    trainer = models.OneToOneField(Staff, on_delete=models.CASCADE, primary_key=True)


class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.SmallIntegerField()
    training = models.ManyToManyField(Trainings)

