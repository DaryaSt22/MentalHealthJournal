from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages, auth

from users.forms import LoginUserForm, SignUpUserForm, ProfileForm
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
                next_url = request.GET.get('next') or 'account'
                return redirect(next_url)
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль')
    else:
        form = LoginUserForm()
    return render(request, 'registration/login.html', {'form': form})


def sign_up_user(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data.get('first_name', '')

            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name
            )

            login(request, user)
            return redirect('account')
    else:
        form = SignUpUserForm()

    return render(request, 'registration/sign_up.html', {'form': form})


@login_required
def account_view(request):
    if request.method == 'POST':
        form = ProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations!")
            return HttpResponseRedirect(reverse('users:account'))
        else:
            form = ProfileForm(instance=request.user)
    user = request.user
    return render(request, 'users/account.html', {'user': user})


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'users/account.html'

@login_required
def logout_account(request):
    auth.logout(request)
    logout(request)
    return render(request, 'registration/logout.html')