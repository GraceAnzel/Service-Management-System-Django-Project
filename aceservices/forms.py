from django import forms
from .models import User,add,payuser
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        widgets = {
            'password': forms.PasswordInput(),
            'cpassword': forms.PasswordInput(),
        }

class GetService(forms.ModelForm):
    class Meta:
        model=add
        fields="__all__"

class Pay(forms.ModelForm):
    class Meta:
        model=payuser
        fields="__all__"