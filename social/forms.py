from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Group, Post

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email','password1','password2')

class createGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'text']

class createPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['message','group']
