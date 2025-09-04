import uuid
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.timezone import now
from journal.models import DailyEntry
from users.models import EmailVerification, Profile, User


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class SignUpUserForm(forms.ModelForm):
    username = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password', 'repeat_password']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('repeat_password'):
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            expiration = now() + timedelta(hours=48)
            record = EmailVerification.objects.create(
                email=uuid.uuid4(), user=user, expiration=expiration
            )
            record.send_verification_email()
        return user


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'goals', 'stress_level', 'avatar', 'day', 'photo', 'activity', 'gratitude',
                  'mood', 'notes']


class EntryForm(forms.ModelForm):
    class Meta:
        model = DailyEntry
        fields = ['goals', 'stress_level', 'day', 'activity', 'gratitude', 'mood', 'notes']
