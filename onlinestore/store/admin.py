from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'urlName')
    list_display_links = ('title', 'id')
    search_fields = ('title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title', 'manufacturer', 'description', 'price', 'in_stock', 'get_photo', 'sort_by', 'created_at',
                    'updated_at',
                    'category', 'ram', 'processor', 'vram', 'hdd_type', 'tyre_section_width', 'tyre_section_height',
                    'season', 'diameter',
                    'category_id', 'search_filter')
    list_display_links = ('title',)
    search_fields = ('title', 'category', 'category')
    list_filter = ('title', 'price', 'category')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        return 'изображение отсутствует'

    get_photo.short_description = 'миниатюра'


class ViewedItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',
                    'title', 'description', 'price', 'get_photo', 'created_at',
                    'updated_at',
                    'number')
    list_display_links = ('title', 'number')
    search_fields = ('title',)
    list_filter = ('title', 'price', 'number')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        return 'изображение отсутствует'

    get_photo.short_description = 'миниатюра'


class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'description', 'sort_by', 'created_at')
    list_display_links = ('category', 'description')
    search_fields = ('category', 'description')
    list_filter = ('category', 'description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ViewedItems, ViewedItemsAdmin)
admin.site.register(SearchQuery, SearchQueryAdmin)
