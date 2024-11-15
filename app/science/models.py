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


class State(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    name = models.CharField(max_length=255, unique=True, verbose_name='Состояние')
    symbol = models.CharField(blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'

    def __str__(self):
        return self.name


class SaturationData(models.Model):
    element = models.ForeignKey(Element, on_delete=models.PROTECT, verbose_name='Элемент')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    temperature = models.FloatField(verbose_name='Температура')
    pressure = models.FloatField(verbose_name='Давление')
    density = models.FloatField(verbose_name='Плотность')
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, verbose_name='Состояние', blank=True)

    class Meta:
        verbose_name = 'Данные линии насыщения'

    def __str__(self):
        return f'Element: {self.element.name}'


class PhaseDiagram(models.Model):
    element = models.ForeignKey(Element, on_delete=models.PROTECT, verbose_name='Элемент')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    temperature = models.FloatField(verbose_name='Температура')
    pressure = models.FloatField(verbose_name='Давление')
    density = models.FloatField(verbose_name='Плотность')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Данные фазовой диаграммы'

    def __str__(self):
        return f'Element: {self.element.name}'


class Storage(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    values = models.JSONField(verbose_name='Значения')
    query = models.CharField(max_length=255, verbose_name='Поисковой запрос')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Хранилище данных'
        verbose_name_plural = 'Хранилище данных'

    def __str__(self):
        return f'Данные пользователя: {self.user.username}'
