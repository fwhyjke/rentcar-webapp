# Generated by Django 4.2.3 on 2023-07-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_alter_user_groups_alter_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifyemailtoken',
            name='token',
            field=models.CharField(),
        ),
    ]
