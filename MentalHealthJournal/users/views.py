from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from users.forms import LoginUserForm, ProfileForm, SignUpUserForm
from users.models import User


class HomeView(TemplateView):
    template_name = 'users/greeting.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['title'] = 'MentalHealthJournal'
        return context


class LoginFormView(FormView):
    template_name = 'registration/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('account')


    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user:
            login(self.request, user)
            next_url = self.request.GET.get('next')
            return redirect(next_url or self.get_success_url())
        else:
            form.add_error(None, 'Неверное имя пользователя или пароль')
            return self.form_invalid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class SignUpFormView(FormView):
    template_name = 'registration/sign_up.html'
    form_class = SignUpUserForm
    success_url = reverse_lazy('account')


    def sign_up_user(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data.get('first_name', '')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name
        )

        login(self.request, user)
        return super().form_valid(form)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class AccountUpdateView(UpdateView):
    model= User
    form_class = ProfileForm
    template_name = 'users/account.html'
    success_url = reverse_lazy('account')

    def get_object(self, queryset=None):
        return self.request.user


class LogOutTemplateView(TemplateView):
    template_name = 'registration/logout.html'
