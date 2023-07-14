from django.contrib import admin

from rentgame_app.models import Game, City, GamesCategory, GamesPlatform

# Register your models here.

models = [Game, City, GamesCategory, GamesPlatform]

for model in models:
    admin.site.register(model)
