from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

    
class UsersForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'input-text with-border', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'input-text with-border', 'placeholder': 'Repeat Password'}))
    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'required': True}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'required': True}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'required': True}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'required': True}),
        }
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1", 
            "password2"
        ]

class UserProfileForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone', 'required': True}),
            'short_description': forms.Textarea(attrs={'placeholder': 'Description', 'required': True})
        }
        model = UserProfile
        fields = [
            "profile_picture",
            "phone_number",
            "short_description",
        ]