from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

from .models import User

from django import forms 


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        # model = get_user_model()
        model = CustomUser
        fields = ['phone', 'email', 'first_name']

class CustomUserForm(UserCreationForm):
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Phone No'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter password'}))
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and len(str(phone)) > 10:
            raise forms.ValidationError('Phone number should not be greater than 10 digits')
        return phone
    
    class Meta:
        model = CustomUser
        fields =  ['phone', 'email','password1', 'password2']



# class CustomUserForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Username'}))
#     email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Email'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter password'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter password'}))
#     class Meta:
#         model = CustomUser
#         fields =  ['phone', 'email','password1', 'password2']