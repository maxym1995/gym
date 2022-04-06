from django.db import models
from datetime import date

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

HOURS = (
    (1, "01:00"),
    (2, "02:00"),
    (3, "03:00"),
    (4, "04:00"),
    (5, "05:00"),
    (6, "06:00"),
    (7, "07:00"),
    (8, "08:00"),
    (9, "09:00"),
    (10, "10:00"),
    (11, "11:00"),
    (12, "12:00"),
    (13, "13:00"),
    (14, "14:00"),
    (15, "15:00"),
    (16, "16:00"),
    (17, "17:00"),
    (18, "18:00"),
    (19, "19:00"),
    (20, "20:00"),
    (21, "21:00"),
    (22, "22:00"),
    (23, "23:00"),
    (24, "24:00")
)


class Members(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
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
    start_time = models.IntegerField(choices = HOURS)
    end_time = models.IntegerField(choices = HOURS)
    date = models.DateField()
    max_participants = models.PositiveIntegerField()

class Rooms(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.SmallIntegerField()
    training = models.ManyToManyField(Trainings)


class Reservations(models.Model):
    member = models.ForeignKey(Members, on_delete = models.CASCADE)
    training = models.ForeignKey(Trainings, on_delete=models.CASCADE)
    msg_to_trainer = models.CharField(max_length=256, null = True)

