from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUserForm(UserCreationForm):

    class meta :
        model=User
        fields=['username','email','password1','password1','is_staff']




class loginUserForm(forms.Form):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))