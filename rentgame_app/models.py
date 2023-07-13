from django.db import models
from users_app.models import User
from rentgame_app.utils import StrMixin


class City(StrMixin, models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Город')


class GamesCategory(StrMixin, models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Категория')


class GamesPlatform(StrMixin, models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Платформа')


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(GamesCategory, on_delete=models.CASCADE, verbose_name='Категория')
    platform = models.ForeignKey(GamesPlatform, on_delete=models.CASCADE, verbose_name='Платформа')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город')
    title = models.CharField(max_length=64, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='slug')
    price = models.IntegerField(verbose_name='Цена')
    pledge = models.IntegerField(blank=True, verbose_name='Залог')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='games_images', blank=True, verbose_name='Изображение')
