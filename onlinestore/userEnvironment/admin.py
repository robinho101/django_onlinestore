from django.contrib import admin
from django.utils.safestring import mark_safe
from userEnvironment.models import *


# Register your models here.
class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'product', 'number', 'price_per_item', 'get_photo', 'total_price', 'is_active', 'created_at',
        'updated_at')
    list_display_links = ('id', 'user', 'product', 'number', 'price_per_item', 'total_price')
    search_fields = ('user', 'product', 'number', 'price_per_item', 'total_price')
    list_filter = ('user', 'product', 'number', 'price_per_item', 'total_price')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        return 'изображение отсутствует'

    get_photo.short_description = 'миниатюра'


class UserSelectionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'product', 'price_per_item', 'get_photo', 'created_at', 'updated_at')
    list_display_links = ('id', 'user', 'product', 'price_per_item')
    search_fields = ('user', 'product', 'price_per_item')
    list_filter = ('user', 'product', 'price_per_item')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        return 'изображение отсутствует'

    get_photo.short_description = 'миниатюра'


admin.site.register(ProductInBasket, ProductInBasketAdmin)
admin.site.register(UserSelection, UserSelectionAdmin)
