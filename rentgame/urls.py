from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rentgame_app.urls')),
    path('account/', include('users_app.urls')),
    re_path('', include('social_django.urls', namespace='social')),
]
