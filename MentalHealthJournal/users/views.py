from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from users.forms import LoginUserForm, SignUpUserForm
from users.models import User


def home(request):
    return render(request, 'users/greeting.html', {'title': 'MentalHealth'})


def custom_login(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('account')
    else:
        form = LoginUserForm()
    return render(request, 'registration/login.html', {'form': form})


def sign_up_user(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            user.first_name = form.cleaned_data.get('first_name', '')
            user.save()
            login(request, user)
            return redirect('account')
    else:
        form = SignUpUserForm()
    return render(request, 'registration/sign_up.html', {'form': form})



def account_view(request):
    return render(request, 'users/account.html')


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'users/account.html'


def logout_account(request):
    logout(request)
    return render(request, 'registration/logout.html')