from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from rentgame_app.forms import GameForm
from rentgame_app.models import Game


def get_game_by_slug(slug: str) -> Game:
    """Получение объявления игры по его слагу"""
    game = Game.objects.get(slug=slug)
    return game


def get_game_field_value_dict(game: Game) -> dict:
    """Получение словаря в формате поле бд: значение"""
    fields = game._meta.get_fields()
    data = {attr.name: getattr(game, attr.name) for attr in fields}
    return data


def _update_game_post(request: HttpRequest, game: Game, form: GameForm) -> None:
    """Вносит изменения в запись таблицы игр"""
    fields = ('category', 'platform', 'city', 'title', 'price', 'pledge', 'description')
    for field in fields:
        setattr(game, field, form.cleaned_data[field])
    if 'image' in request.FILES:
        game.image = request.FILES['image']
    else:
        if 'image-clear' in request.POST:
            game.image = None
    game.save()


def update_game_post_or_return_error(request: HttpRequest, game: Game, form: GameForm) -> HttpResponse:
    """Если форма содержит правильные данные, обновляет запись в бд и переадрессовывает пользователя
    на страницу с объявлением, иначе не отправляет изменения и рендерит страницу редактирования записи
    с отображающимеся ошибками в форме"""
    if form.is_valid():
        _update_game_post(request, game, form)
        return redirect('show', game_slug=game.slug)
    else:
        template = 'rentgame_app/change_game.html'
        context = {'game': game, 'form': form}
        return render(request, template_name=template, context=context)
