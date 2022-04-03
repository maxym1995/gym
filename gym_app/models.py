from django.db import models

# Create your models here.
# from gym_app.models import *

SEX = (
    (0, "Female"),
    (1, "Male"),

)

class Members(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    sex = models.IntegerField(choices=SEX)
    year_of_birth = models.IntegerField(null=True)

