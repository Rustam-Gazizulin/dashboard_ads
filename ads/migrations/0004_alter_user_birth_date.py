# Generated by Django 4.1.7 on 2023-03-06 12:45

import ads.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_user_birth_date_alter_ads_is_published_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(
                validators=[ads.models.birth_date_validator],
                verbose_name="Дата рождения",
            ),
        ),
    ]