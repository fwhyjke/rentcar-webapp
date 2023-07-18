from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from rentgame_app.forms import RegistrationForm, LoginForm, GameForm
from rentgame_app.models import Game
from rentgame_app.services import get_game_by_slug, get_game_field_value_dict, update_game_post_or_return_error


# welcome page view
class MainPageView(ListView):
    model = Game
    template_name = 'rentgame_app/main.html'
    context_object_name = 'games'

    def get_queryset(self):
        return Game.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'RentGame: аренда игр'
        return context


class AddGameView(CreateView):
    template_name = 'rentgame_app/addgame.html'
    form_class = GameForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание объявления'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('show', kwargs={'game_slug': self.object.slug})


#
class ChangeGameView(View):
    def get(self, request, *args, **kwargs):
        template = 'rentgame_app/change_game.html'

        slug = kwargs['game_slug']
        game = get_game_by_slug(slug=slug)
        initial = get_game_field_value_dict(game)
        form = GameForm(initial=initial)
        context = {'game_title': initial['title'], 'form': form, 'slug': slug}

        return render(request, template_name=template, context=context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        game = get_game_by_slug(slug=kwargs['game_slug'])
        form = GameForm(request.POST, request.FILES)

        return update_game_post_or_return_error(request, game, form)


class ShowGameView(View):
    def get(self, request, *args, **kwargs):
        template = 'rentgame_app/show_game.html'
        game = get_game_by_slug(slug=kwargs['game_slug'])
        context = get_game_field_value_dict(game)
        context['page_title'] = context['title'] + ': просмотр объявления'
        context['active_user'] = self.request.user

        return render(request, template_name=template, context=context)


#

# registration page view
class RegistrationView(CreateView):
    template_name = 'rentgame_app/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        # Since we have no only one backend, we need to specify which one to use here
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user)
        return redirect('main')


class LoginUserView(LoginView):
    template_name = 'rentgame_app/login.html'
    form_class = LoginForm


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('main')
