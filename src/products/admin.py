from django.contrib import admin
from .models import Gallery, Product


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'