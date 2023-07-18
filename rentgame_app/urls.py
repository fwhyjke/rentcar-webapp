from django.urls import path
from rentgame_app.views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('addgame', AddGameView.as_view(), name='addgame'),
    path('registration', RegistrationView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', LogoutUserView.as_view(), name='logout'),
    path('game/<slug:game_slug>', ShowGameView.as_view(), name='show'),
    path('game/change/<slug:game_slug>', ChangeGameView.as_view(), name='change'),
]
