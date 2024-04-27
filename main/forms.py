from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DoctorRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length = 20, label='First Name')
    last_name = forms.CharField(max_length = 20, label='Last Name')
    username = forms.CharField(max_length = 20, label='Username Name')
    email = forms.EmailField(max_length=200, help_text='Required', label='Email')
    password1 = forms.CharField(max_length = 20, label='Password')
    password2 = forms.CharField(max_length = 20, label='Confirm password')


    class Meta:
        model = User
        fields = ['First Name','Last Name', 'username', 'email', 'password1', 'password2']
    

class PatientRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length = 20, label='First Name')
    last_name = forms.CharField(max_length = 20, label='Last Name')
    username = forms.CharField(max_length = 20, label='Username Name')
    email = forms.EmailField(max_length=200, help_text='Required', label='Email')
    password1 = forms.CharField(max_length = 20, label='Password')
    password2 = forms.CharField(max_length = 20, label='Confirm password')


    class Meta:
        model = User
        fields = ['First Name','Last Name', 'username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)