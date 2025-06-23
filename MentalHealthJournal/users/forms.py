from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User
from django.contrib.auth.forms import UserCreationForm


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

# class SignUpUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']

# class SignUpUserForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

class SignUpUserForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('repeat_password'):
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data



# class CustomUserCreationForm(forms.Form):
#     username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#     password2 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']