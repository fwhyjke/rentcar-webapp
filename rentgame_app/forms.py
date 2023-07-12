from users_app.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        data = self.cleaned_data
        data['password'] = data.pop('password1')
        del data['password2']
        user = User.objects.create_user(**data)
        return user


class LoginForm(AuthenticationForm):
    None
