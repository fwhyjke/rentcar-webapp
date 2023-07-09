from django.shortcuts import render
from django.views.generic import TemplateView


# welcome page view
class WelcomePage(TemplateView):
    template_name = 'welcome.html'
