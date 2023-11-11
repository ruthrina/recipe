from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets ={
            'username':forms.TextInput(attrs={'class':'input'}),
            'email':forms.TextInput(attrs={'class':'input'}),
            'password1':forms.TextInput(attrs={'class':'input'}),
            'password2':forms.TextInput(attrs={'class':'input'}),
        }


