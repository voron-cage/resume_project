# Generated by Django 5.0.3 on 2024-03-21 14:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Имя')),
                ('surname', models.CharField(max_length=240, verbose_name='Фамилия')),
                ('icon', models.ImageField(null=True, upload_to='', verbose_name='Иконка')),
                ('description', models.TextField(blank=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователя',
            },
        ),
    ]
