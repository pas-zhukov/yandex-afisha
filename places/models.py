from dataclasses import dataclass
from decimal import Decimal

from django.db import models


@dataclass
class Coordinates:
    latitude: Decimal
    longitude: Decimal

    def __str__(self):
        return f'{round(self.latitude, 5)} {round(self.longitude, 5)}'


class Place(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.lat and self.long:
            self.coordinates = Coordinates(latitude=self.lat, longitude=self.long)

    title = models.CharField(max_length=200, verbose_name='Название', null=True)
    description_short = models.TextField(verbose_name='Краткое описание', null=True)
    description_long = models.TextField(verbose_name='Полное описание', null=True)
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
        blank=False,
        null=False,
    )
    title = models.CharField(max_length=200, verbose_name='Название', null=True, blank=True)
    image = models.ImageField(verbose_name='Картинка', null=True)
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING, related_name='pictures', verbose_name='Место', null=True, blank=True)

    class Meta:
        ordering = ['order_num', ]
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        if self.title:
            return f'{self.id}. {self.title.strip()}'
        else:
            return f'Picture #{self.id}'