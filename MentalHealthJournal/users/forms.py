from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

#class SignUpUserForm(forms.Form):
    # class Meta:
    #     model = User
    #     fields = ('email', 'organization_name')
    #     labels = {
    #         'email': 'Электронная почта',
    #         'organization_name': 'Название организации',
    #     }
    #username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    #password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    #repeat_password = forms.CharField(label='Password (repeat)', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class SignUpUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')




class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))