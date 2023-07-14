from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from rentgame_app.forms import RegistrationForm, LoginForm, AddGameForm


# welcome page view
class MainPageView(CreateView):
    template_name = 'rentgame_app/main.html'
    form_class = AddGameForm
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Аренда авто'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddGameView(CreateView):
    template_name = 'rentgame_app/addgame.html'
    form_class = AddGameForm
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание объявления'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# registration page view
class RegistrationView(CreateView):
    template_name = 'rentgame_app/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        # Since we have no only one backend, we need to specify which one to use here
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user)
        return redirect('main')


class LoginUserView(LoginView):
    template_name = 'rentgame_app/login.html'
    form_class = LoginForm


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('main')
