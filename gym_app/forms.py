from django import forms
from .models import SEX, Members, TYPES, TRAININGS, User, Trainers, HOURS
from django.db import models
from django.core.validators import EmailValidator, URLValidator, ValidationError
from django.contrib.auth.models import User
import string


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


class LoginForm(forms.Form):
    login = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

class AddUserForm(UserForm):
    password_1 = forms.CharField(widget=forms.PasswordInput,
                                 help_text="Type password twice")
    password_2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        if User.objects.filter(username=self.data['username']).exists():
            self.add_error('username', error='User already exsist')
        return self.data['username']

    def clean(self):
        numbers = False
        special_char = False

        for char in self.data['password_1']:
            if char in string.digits:
                numbers = True

        for char in self.data['password_1']:
            if char in string.punctuation:
                special_char = True

        if self.data['password_1'] != self.data['password_2']:
            self.add_error(None, error='Password is not matching!')
        elif len(self.data['password_1']) < 8:
            self.add_error(None, error='Password must contains at least 8 characters!')
        elif (self.data['password_1']).islower():
            self.add_error(None, error='At least 1 uppercase required!')
        elif (self.data['password_1']).isupper():
            self.add_error(None, error='At least 1 lowercase required!')
        elif numbers != True:
            self.add_error(None, error='At least 1 number required!')
        elif special_char != True:
            self.add_error(None, error='At least 1 special character required!')
        return super().clean()


    def save(self):
        user_data = self.cleaned_data
        user = User.objects.create_user(
            username=user_data['username'],
            password=user_data['password_1'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
        )
        return user

    class Meta(UserForm.Meta):
        fields = UserForm.Meta.fields + ('password_1', 'password_2')

class AddRoomForm(forms.Form):
    name = forms.CharField(label="Name", max_length = 64)
    capacity = forms.IntegerField(label = "Capacity", min_value=1, max_value=18)
    training = forms.ChoiceField(label = "Training type", choices = TRAININGS)


class AddTrainerForm(forms.Form):
    user = forms.ModelChoiceField(label = "User",  queryset = User.objects.all())
    training_type = forms.ChoiceField(label = "Training type", choices=TRAININGS)


class AddTrainingForm(forms.Form):
    name = forms.ChoiceField(label = "Training type", choices = TRAININGS)
    trainer = forms.ModelChoiceField(label = "User",  queryset = Trainers.objects.all())
    start_time = forms.ChoiceField(label = "Start time", choices = HOURS)
    end_time = forms.ChoiceField(label = "End time", choices = HOURS)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    max_participants = forms.IntegerField(label ="Max participants", min_value = 1)