from django.urls import path
from rentcar_app.views import WelcomePage

urlpatterns = [
    path('welcome', WelcomePage.as_view()),
]
