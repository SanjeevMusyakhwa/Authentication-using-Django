from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your full name'}), help_text=''
    )
    username = forms.CharField(
      max_length=50, 
      widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Enter your username'}), help_text=''
      )
    email = forms.EmailField(
      widget=forms.EmailInput(attrs={'class':'form-control' ,'placeholder':'Enter your email'}), help_text=''
      )
    phone_number = forms.CharField(
      max_length=20, 
      widget=forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Enter your phone_number'}), help_text=''
      )
    
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control' ,'placeholder': 'Enter your password'}),
        help_text='',  # Remove the help text
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class':'form-control' ,'placeholder': 'Confirm your password'}),
        help_text='',  # Remove the help text
    )
    
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone_number', 'password1', 'password2']
