from collections import Counter

from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView

from journal.models import DailyEntry
from users.forms import EntryForm, LoginUserForm, ProfileForm, SignUpUserForm
from users.models import Profile, User


class HomeView(TemplateView):
    template_name = 'users/greeting.html'
    title = 'MentalHealthJournal'


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
    template_name = 'users/account.html'
    success_url = reverse_lazy('account')

    def get(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = ProfileForm(instance=profile)
        return render(request, self.template_name, {'form': form, 'user': request.user})

    def post(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form, 'user': request.user})


class JournalView(View):
    template_name = 'users/account.html'

    def get(self, request):
        form = EntryForm()
        entries = self.get_entries(request)
        mood_counts = Counter(entry.mood for entry in entries if entry.mood)

        return render(request, self.template_name, {
            'form': form,
            'entries': entries,
            'mood_data': dict(mood_counts)
        })

    def post(self, request):
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('account')

        entries = self.get_entries(request)
        mood_counts = Counter(entry.mood for entry in entries if entry.mood)

        return render(request, self.template_name, {
            'form': form,
            'entries': entries,
            'mood_data': dict(mood_counts)
        })

    def get_entries(self, request):
        return DailyEntry.objects.filter(user=request.user).order_by('-created_at')


class LogOutTemplateView(TemplateView):
    template_name = 'registration/logout.html'