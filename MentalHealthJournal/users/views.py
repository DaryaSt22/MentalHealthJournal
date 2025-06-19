from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginUserForm, SignUpUserForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from users.models import User



def home(request):
    context = {
        'title': 'MentalHealth',
    }
    return render(request, 'users/greeting.html', context)


def authorization(request):
    context = {
        'form': 'SignUpUserForm',
    }
    return render(request, 'registration/login.html', context)


def custom_login(request):
    form = LoginUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                repeat_password=form.cleaned_data['repeat password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/login')
            else:
                form.add_error(None, "Неверные данные")

    return render(request, 'registration/login.html', {'form': form})


def registration(request):
    context = {
        'form': 'SignUpUserForm',
    }
    return render(request, 'registration/sign_up.html', context)

def sign_up_user(request):
    form = SignUpUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                repeat_password=form.cleaned_data['repeat password'],
            )
            if user is not None:
                sign_up_user(request, user)
                return redirect('')
            else:
                form.add_error(None, "Неверные данные")

    return render(request, 'registration/sign_up.html', {'form': form})


def account_view(request):
    return render(request, 'users/account.html')

def logout_account(request):
    return render(request, 'registration/logout.html')


def sign_up_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/account')