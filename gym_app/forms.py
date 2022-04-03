from django import forms
from .models import SEX, Members, TYPES
from django.db import models
from django.core.validators import EmailValidator, URLValidator, ValidationError
from django.contrib.auth.models import User


class AddMemberForm(forms.Form):
    first_name = forms.CharField(label="Name", max_length = 64)
    last_name = forms.CharField(label="Surname", max_length= 64)
    year_of_birth = forms.IntegerField(label = "Year of birth", min_value=1900, max_value=2022)
    sex = forms.ChoiceField(label = "Sex", choices = SEX)


class AddStaffForm(forms.Form):
    first_name = forms.CharField(label="Name", max_length = 64)
    last_name = forms.CharField(label="Surname", max_length= 64)
    year_of_birth = forms.IntegerField(label = "Year of birth", min_value=1900, max_value=2022)
    type = forms.ChoiceField(label = "Training type", choices = TYPES)