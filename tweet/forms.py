from django import forms 
import django.contrib.auth.models
import django.db
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Tweetform(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]