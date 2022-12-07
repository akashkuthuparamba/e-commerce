from django.forms import ModelForm
from . models import item
from django.contrib.auth.models import User

class ItemForm(ModelForm):
    class Meta:
        model=item
        fields='__all__'

class LoginForm(ModelForm):
    class Meta:
        model=User
        fields=("username","password")


class RegisterForm(ModelForm):
    class Meta:
        model=User
        fields=("username","password","email")        