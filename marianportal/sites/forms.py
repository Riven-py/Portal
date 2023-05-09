from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Module, Subject

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'middle_initial', 'last_name', 'role')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'middle_initial', 'last_name', 'role')

class CustomUserLoginForm(forms.Form):
    id = forms.CharField(max_length=10, label='School ID')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())

class UploadForm(forms.ModelForm):
        
    class Meta:
        model = Module
        fields = ['file', 'title', 'description', 'subject']
        widgets = {'uploaded_by': forms.HiddenInput()}
