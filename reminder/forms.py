from django import forms
from reminder.models import Todos
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from reminder.models import Todos


class Userform(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]



# registration,login,logout

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class TodoForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["name"]