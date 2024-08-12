from django.contrib.auth.forms import UserCreationForm
from .models import User, Note
from django.forms import ModelForm
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'bio']




