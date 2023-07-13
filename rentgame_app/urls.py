from django.urls import path
from rentgame_app.views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
]
