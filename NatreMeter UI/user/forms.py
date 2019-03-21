from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import sign

#class UserRegisterForm(UserCreationForm):
#    email = forms.EmailField()
    #Age  = forms.IntegerField()

#    class Meta:
#        model = User
        # fields=['username','email','password1','password2']
class signForm(forms.ModelForm):
    class Meta:
        model = sign
        fields = [
        'Phone',
        'Age',
        'Gender'
        ]
