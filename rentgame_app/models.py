from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

from users_app.models import User
from rentgame_app.utils import StrMixin, generate_random_string


class City(StrMixin, models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class GamesCategory(StrMixin, models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории игр'


class GamesPlatform(StrMixin, models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Платформа')

    class Meta:
        verbose_name = 'Игровая платформа'
        verbose_name_plural = 'Игровые платформы'


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(GamesCategory, on_delete=models.CASCADE, verbose_name='Категория')
    platform = models.ForeignKey(GamesPlatform, on_delete=models.CASCADE, verbose_name='Платформа')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name='Город')
    title = models.CharField(max_length=64, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='slug')
    price = models.IntegerField(verbose_name='Цена')
    pledge = models.IntegerField(verbose_name='Залог')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='games_images', blank=True, verbose_name='Изображение')

    def save(self, *args, **kwargs):
        # slug generate
        if not self.slug:
            slug_list = Game.objects.values_list('slug', flat=True)
            slug = slugify(unidecode(self.title))
            if slug in slug_list:
                slug += f'-{generate_random_string(6)}'
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Объявление по продаже игр'
        verbose_name_plural = 'Объявления по продаже игр'
