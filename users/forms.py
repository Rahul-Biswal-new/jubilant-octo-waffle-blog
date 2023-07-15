from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # emails = forms.EmailField() 

    # age = forms.IntegerField()
    address = forms.CharField()
    # gender = forms.CharField()



    class Meta:
        model = User
        fields = ['username', 'email' ,  'address', 'password1', 'password2']


