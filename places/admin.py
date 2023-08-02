from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Picture


class PlacePicturesInline(admin.TabularInline):
    model = Picture
    fields = ['image', 'image_preview', 'order_num']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width='auto',
            height=200,
        ))


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ['coords']
    inlines = [PlacePicturesInline]
    sortable_by = ['id', 'title']

    def coords(self, obj):
        return f'{obj.coordinates}'


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_preview', 'place']

    def image_preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width='auto',
            height=100,
        ))