from django.contrib.auth.models import User
from django.db import models


class Element(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'
