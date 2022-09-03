from django.contrib import admin
from .models import Category, Product
from django.utils.safestring import mark_safe


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    list_display_links = ('title', 'id')
    search_fields = ('title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title', 'manufacturer', 'description', 'price', 'in_stock', 'get_photo', 'created_at',
                    'updated_at',
                    'category',
                    'category_id')
    list_display_links = ('title',)
    search_fields = ('title', 'category')
    list_filter = ('title', 'price')

    # fields = (
    #     'title', 'manufacturer', 'description', 'price', 'get_photo', 'created_at', 'updated_at',
    #     'category')
    # readonly_fields = ('get_photo', 'created_at', 'updated_at')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        return 'изображение отсутствует'

    get_photo.short_description = 'миниатюра'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
