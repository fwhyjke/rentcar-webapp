from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from rentgame_app.forms import RegistrationForm, LoginForm


# welcome page view
class WelcomeView(TemplateView):
    template_name = 'rentgame_app/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Аренда авто'
        return context


# registration page view
class RegistrationView(CreateView):
    template_name = 'rentgame_app/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('welcome')


class LoginUserView(LoginView):
    template_name = 'rentgame_app/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('welcome')


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('welcome')
