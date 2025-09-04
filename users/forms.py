from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [
            'user_type',
            'first_name',
            'last_name',
            'profile_pic',
            'username',
            'email',
            'password1',
            'password2',
            'address_line1',
            'city',
            'state',
            'pincode',
        ]
