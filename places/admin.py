from django.contrib import admin
from .models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ['coords']

    def coords(self, obj):
        return f'{obj.coordinates}'
