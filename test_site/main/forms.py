from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
# LANGUAGE_CHOICES = [
#     ('nodejs', 'NodeJs'),
#     ('java', 'Java'),
#     ('python', 'Python'),
# ]
#
#
# class LanguageForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     age = forms.IntegerField()
#     favorite_fruit = forms.CharField(label='What is your favorite fruit?',
#                                      widget=forms.Select(choices=LANGUAGE_CHOICES))
