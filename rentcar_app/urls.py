from django.urls import path
from rentcar_app.views import *

urlpatterns = [
    path('welcome', WelcomeView.as_view(), name='welcome'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout')
]
