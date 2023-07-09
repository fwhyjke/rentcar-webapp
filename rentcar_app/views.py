from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from rentcar_app.forms import RegistrationForm


# welcome page view
class WelcomeView(TemplateView):
    template_name = 'welcome.html'


# registration page view
class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('welcome')