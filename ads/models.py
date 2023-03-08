import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils.text import slugify
from django.core.validators import ValidationError


USER_MIN_AGE = 9


def validate_is_published(value):
    if value:
        raise ValidationError('Значение поля is_published не может быть True')


def birth_date_validator(value: datetime.date):
    today = datetime.date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < USER_MIN_AGE:
        raise ValidationError("В сервисе могут зарегистрироваться люди старше 9 лет")


def validate_email(value):
    if value.endswith('rambler.ru'):
        raise ValidationError('Нельзя зарегистрировать email с доменом rambler.ru')


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Категория', unique=True)
    slug = models.SlugField(unique=True, validators=[MinLengthValidator(5)], max_length=10, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:10]
        super(Category, self).save(*args, **kwargs)

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


class User(AbstractUser):
    STATUS = [
        ('member', 'Пользователь'),
        ('admin', 'Администратор'),
        ('moderator', 'Модератор')
    ]
    role = models.CharField(choices=STATUS, max_length=20, default='member', verbose_name='Должность')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', null=True, blank=True)
    location_id = models.ManyToManyField(Location, verbose_name='Адрес')
    birth_date = models.DateField(validators=[birth_date_validator], verbose_name='Дата рождения')
    email = models.EmailField(verbose_name='Почта', validators=[validate_email])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Ads(models.Model):
    name = models.CharField(max_length=100, verbose_name='Объявление', validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='ads')
    price = models.PositiveBigIntegerField(verbose_name='Цена', validators=[MinValueValidator(0)])
    description = models.TextField(max_length=1000, verbose_name='Описание', null=True)
    is_published = models.BooleanField(verbose_name='Статус объявления', default=False,
                                       validators=[validate_is_published])
    image = models.ImageField(upload_to='images/', verbose_name='Фото', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, verbose_name='Категория', related_name='cat')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-price']

    def __str__(self):
        return self.name


class Selection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='selections')
    name = models.CharField(max_length=50, unique=True, verbose_name='Подборка')
    items = models.ManyToManyField(Ads)

    class Meta:
        verbose_name = 'Подборка объявлений'
        verbose_name_plural = 'Подборки объявлений'

    def __str__(self):
        return self.name



