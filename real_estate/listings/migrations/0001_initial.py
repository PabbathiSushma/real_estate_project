# Generated by Django 4.2 on 2023-05-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Listings",
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
                ("title", models.CharField(max_length=150)),
                ("price", models.IntegerField()),
                ("nums_bedrooms", models.IntegerField()),
                ("nums_bathrooms", models.IntegerField()),
                ("sqaure_footage", models.IntegerField()),
                ("address", models.CharField(max_length=200)),
            ],
        ),
    ]
