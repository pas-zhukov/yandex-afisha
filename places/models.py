from dataclasses import dataclass
from decimal import Decimal
from tinymce.models import HTMLField
from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = HTMLField(verbose_name='Полное описание')
    lat = models.DecimalField(max_digits=20, decimal_places=16, verbose_name='Широта',)
    long = models.DecimalField(max_digits=20, decimal_places=16, verbose_name='Долгота')

    class Meta:
        ordering = ['id']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return f'{self.id}. {self.title.strip()}'


class Picture(models.Model):
    order_num = models.PositiveIntegerField(
        default=0,
        blank=True,
    )
    title = models.CharField(max_length=200, verbose_name='Название', blank=True)
    image = models.ImageField(verbose_name='Картинка', blank=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='pictures', verbose_name='Место', blank=False)

    class Meta:
        ordering = ['order_num', ]
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        if self.title:
            return f'{self.id}. {self.title.strip()}'
        else:
            return f'Picture #{self.id}'
