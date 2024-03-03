from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User


class LoginForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    state = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    pincode = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'profile_picture', 'city', 'state', 'pincode', 'username', 'email', 'password1', 'password2', 'is_admin', 'is_Patient', 'is_Doctor')
