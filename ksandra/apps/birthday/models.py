from django.db import models
import datetime
from django.utils import timezone

class Prize(models.Model):
    code = models.CharField('Код', max_length=6)
    prize = models.CharField('Награда', max_length=50)
    poem = models.TextField('Стих', blank=True)
    poem_choose = models.CharField('Выбор стиха', max_length=6, blank=True)
    status = models.BooleanField('Статус выполнения')
    activated = models.BooleanField('Активирован')
    time_activate = models.DateTimeField('Время активации')
    image = models.ImageField('Изображение', upload_to='image/')
    image_add_one = models.ImageField('Изображение 1', upload_to='image/', blank=True)
    image_add_two = models.ImageField('Изображение 2', upload_to='image/', blank=True)
    image_add_three = models.ImageField('Изображение 3', upload_to='image/', blank=True)

    def __str__(self):
        return self.code

    def activation(self):
        return self.time_activate >= (timezone.now() - datetime.timedelta(days=1))

    class Meta:
        verbose_name = 'Код'
        verbose_name_plural = 'Коды'