from django.shortcuts import redirect
from rest_framework.views import APIView
from users_app.models import VerifyEmailToken


# I think I don't need a serializer since I only change one field
class VerifyEmail(APIView):
    def get(self, request, **kwargs):
        token = self.kwargs['token']
        user = VerifyEmailToken.objects.get(token=token).user
        user.is_verified = True
        user.save()
        return redirect('welcome')