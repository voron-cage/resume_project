from django.db import models


class UserProfile(models.Model):
    name = models.CharField('Имя', max_length=240, blank=True)
    surname = models.CharField('Фамилия', max_length=240, blank=True)
    icon = models.ImageField('Иконка', null=True)
    description = models.TextField(blank=True)
    user = models.OneToOneField('auth.User', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователя'

    def __str__(self):
        return self.user.username
