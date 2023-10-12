from django.contrib.auth.models import User
from django.db import models


class Element(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    name = models.CharField(max_length=255, unique=True, verbose_name='Имя')
    symbol = models.CharField(max_length=255, unique=True, verbose_name='Символ')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

    def __str__(self):
        return self.name
