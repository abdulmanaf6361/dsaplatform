from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=False, label='Last Name')
    batch_name = forms.CharField(required=True, label='Batch Name', 
                                  help_text='e.g. DSA Batch July 2026')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'batch_name', 'password1', 'password2']
