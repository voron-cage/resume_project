# Generated by Django 5.0.3 on 2024-03-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=240, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='surname',
            field=models.CharField(blank=True, max_length=240, verbose_name='Фамилия'),
        ),
    ]
