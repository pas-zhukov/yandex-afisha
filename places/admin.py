from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Picture
from adminsortable2.admin import SortableTabularInline, SortableAdminMixin


class PlacePicturesInline(SortableTabularInline):
    model = Picture
    fields = ['image', 'image_preview', 'order_num']
    readonly_fields = ['image_preview', 'order_num']
    extra = 0

    def image_preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width='auto',
            height=100,
        ))


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['coords']
    inlines = [PlacePicturesInline]
    sortable_by = ['id', 'title']
    search_fields = ['title']

    def coords(self, obj):
        return f'{obj.coordinates}'
