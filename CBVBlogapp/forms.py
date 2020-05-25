from django import forms
from django.contrib.auth.models import User
from .models import Blogs



class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {'password':forms.PasswordInput()}


class UploadForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields = ('Title','Description','postedby','pic')
