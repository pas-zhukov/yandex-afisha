from django.contrib import admin
from .models import Place, Picture


class PlacePicturesInline(admin.TabularInline):
    model = Picture
    fields = ['image', 'title', 'order_num']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ['coords']
    inlines = [PlacePicturesInline]
    sortable_by = ['id', 'title']

    def coords(self, obj):
        return f'{obj.coordinates}'


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'place']