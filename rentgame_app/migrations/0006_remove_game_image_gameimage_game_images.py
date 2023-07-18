# Generated by Django 4.2.3 on 2023-07-16 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentgame_app', '0005_game_image_delete_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='image',
        ),
        migrations.CreateModel(
            name='GameImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='games_images', verbose_name='Изображение')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_images', to='rentgame_app.game', verbose_name='Игра')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='games', to='rentgame_app.gameimage', verbose_name='Изображения'),
        ),
    ]
