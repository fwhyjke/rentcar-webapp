from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from rentcar_app.forms import RegistrationForm, LoginForm


# welcome page view
class WelcomeView(TemplateView):
    template_name = 'welcome.html'


# registration page view
class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('welcome')


class LoginUserView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('welcome')