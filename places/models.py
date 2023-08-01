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

    title = models.CharField(max_length=200, null=True)
    description_short = models.TextField(null=True)
    description_long = models.TextField(null=True)
    lat = models.DecimalField(max_digits=20, decimal_places=16)
    long = models.DecimalField(max_digits=20, decimal_places=16)

    def __str__(self):
        return f'{self.id}. {self.title.strip()}'
