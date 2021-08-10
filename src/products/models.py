from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=50, help_text="Добавьте название товара")
    # classific = models.CharField('Класс', max_length=50, help_text="Добавьте класс товара")
    description = models.TextField('Описание', max_length=350, help_text="Добавьте описание товара")
    image = models.ImageField('Картинка', upload_to='products', null=True, default=None)
    image2 = models.ImageField('Вторая Картинка', upload_to='products', null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Gallery(models.Model):
    image = models.ImageField('Картинка', upload_to='gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
