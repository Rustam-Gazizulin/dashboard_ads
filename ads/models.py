from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name='Адрес')
    lat = models.DecimalField(max_digits=8, decimal_places=6, verbose_name='Долгота', null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, verbose_name='Широта', null=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class User(models.Model):
    STATUS = [
        ('member', 'Пользователь'),
        ('admin', 'Администратор'),
        ('moderator', 'Модератор')
    ]

    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    username = models.CharField(max_length=30, unique=True, verbose_name='Ник')
    password = models.CharField(max_length=50, unique=True)
    role = models.CharField(choices=STATUS, max_length=20, default='member', verbose_name='Должность')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', null=True)
    location_id = models.ManyToManyField(Location, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Ads(models.Model):
    name = models.CharField(max_length=100, verbose_name='Объявление')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='ads')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    description = models.TextField(max_length=1000, verbose_name='Описание', null=True)
    is_published = models.BooleanField(verbose_name='Статус объявления', default=False)
    image = models.ImageField(upload_to='image/', verbose_name='Фото', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='cat')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-price']

    def __str__(self):
        return self.name



