# Generated by Django 4.1.7 on 2023-02-19 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="Категория"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Адрес")),
                (
                    "lat",
                    models.DecimalField(
                        decimal_places=6,
                        max_digits=8,
                        null=True,
                        verbose_name="Долгота",
                    ),
                ),
                (
                    "lng",
                    models.DecimalField(
                        decimal_places=6, max_digits=8, null=True, verbose_name="Широта"
                    ),
                ),
            ],
            options={
                "verbose_name": "Локация",
                "verbose_name_plural": "Локации",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=30, verbose_name="Фамилия")),
                (
                    "username",
                    models.CharField(max_length=30, unique=True, verbose_name="Ник"),
                ),
                ("password", models.CharField(max_length=50, unique=True)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("member", "Пользователь"),
                            ("admin", "Администратор"),
                            ("moderator", "Модератор"),
                        ],
                        default="member",
                        max_length=20,
                        verbose_name="Должность",
                    ),
                ),
                (
                    "age",
                    models.PositiveSmallIntegerField(null=True, verbose_name="Возраст"),
                ),
                (
                    "location",
                    models.ManyToManyField(to="ads.location", verbose_name="Адрес"),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.CreateModel(
            name="Ads",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Объявление")),
                ("price", models.PositiveBigIntegerField(verbose_name="Цена")),
                (
                    "description",
                    models.TextField(
                        max_length=1000, null=True, verbose_name="Описание"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False, verbose_name="Статус объявления"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="image/", verbose_name="Фото"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ads",
                        to="ads.user",
                        verbose_name="Автор",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cat",
                        to="ads.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
                "ordering": ["-price"],
            },
        ),
    ]
