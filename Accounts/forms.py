from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from Accounts.models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    age = forms.CharField(widget=forms.NumberInput())

    class Meta:
        model = User

        fields = ('username', 'email', 'password1', 'password2')




class EditProfile(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'class': 'button3'}))

    class Meta:
        model = Profile
        fields = ('photo', )
