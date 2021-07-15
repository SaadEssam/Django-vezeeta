from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput




class Login_Form(forms.ModelForm):
    username = forms.CharField(label='الاسم')
    password = forms.CharField(label='كلمة المرور' , widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password')