from django.db import models


class Carousel(models.Model):
    image = models.FileField(verbose_name='Картинка')
    caption = models.TextField()
    body = models.TextField()

    class Meta:
        verbose_name = 'Предмет карусели'
        verbose_name_plural = 'Предметы карусели'

    def __str__(self):
        return f'{self.caption}'
