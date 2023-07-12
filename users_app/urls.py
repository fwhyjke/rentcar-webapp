from django.urls import path
from users_app.views import VerifyEmail

urlpatterns = [
    path('confirm-email/<str:token>', VerifyEmail.as_view())
]
