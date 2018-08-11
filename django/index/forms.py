from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import Profile
from django import forms



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','location','birth_date')

class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password", max_length=100, widget=forms.PasswordInput)



    def clean_user(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        #TODO: figure out what to clean

        return username, password


class RegistrationForm(UserCreationForm):
    #add the email and first and last name
    # email is required and first and last name are optional

    email = forms.EmailField(required=True)

    class Meta:
        model =User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


