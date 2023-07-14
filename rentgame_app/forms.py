from django.forms import ModelForm, HiddenInput, ModelChoiceField
from rentgame_app.models import Game, City, GamesCategory, GamesPlatform
from users_app.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import Select, ValidationError


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


class AddGameForm(ModelForm):
    category = ModelChoiceField(queryset=GamesCategory.objects.all(), empty_label='Выберите категорию игры', widget=Select)
    platform = ModelChoiceField(queryset=GamesPlatform.objects.all(), empty_label='Выберите игровую платформу', widget=Select)
    city = ModelChoiceField(queryset=City.objects.all(), empty_label='Выберите город', widget=Select)

    class Meta:
        model = Game
        fields = ('category', 'platform', 'city', 'title', 'price', 'pledge', 'description', 'image')
        widgets = {
            'user': HiddenInput(),
            'slug': HiddenInput(),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def clean_pledge(self):
        pledge = self.cleaned_data.get('pledge')
        if pledge is not None and pledge < 0:
            raise ValidationError('Залог не может быть отрицательным')
        return pledge
