from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'})
    )
    username = forms.CharField(
      max_length=50, 
      widget=forms.TextInput(attrs={'placeholder':'Enter your username'})
      )
    email = forms.EmailField(
      widget=forms.EmailInput(attrs={'placeholder':'Enter your email'})
      )
    phone_number = forms.CharField(
      max_length=20, 
      widget=forms.TextInput(attrs={'placeholder':'Enter your phone_number'})
      )
    

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone_number', 'password1', 'password2']
