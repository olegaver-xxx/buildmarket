from django.db import models
class Product(models.Model):
    Название_Товара = models.CharField(max_length=50, help_text="Добавьте название товара")
    Описание_Товара = models.TextField(max_length=350, help_text="Добавьте описание товара")

    def __str__(self):
        return self.Название_Товара

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
class Gallery(models.Model):
    image = models.ImageField(upload_to='media')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Изображения')
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'