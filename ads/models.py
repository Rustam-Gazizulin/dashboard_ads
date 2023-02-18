from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name


class Ads(models.Model):
    name = models.CharField(max_length=100, verbose_name='Объявление')
    author = models.CharField(max_length=50, verbose_name='Автор')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    description = models.TextField(max_length=1000, verbose_name='Описание', null=True)
    address = models.CharField(max_length=500, verbose_name='Адрес')
    is_published = models.BooleanField(verbose_name='Статус объявления', default=False)
