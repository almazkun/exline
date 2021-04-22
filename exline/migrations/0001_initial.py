# Generated by Django 3.2 on 2021-04-21 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("city_id", models.IntegerField(unique=True, verbose_name="City id")),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="City name"
                    ),
                ),
                (
                    "cached_path",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="Province"
                    ),
                ),
                ("zone", models.CharField(max_length=50, verbose_name="Zone")),
                ("origin", models.BooleanField(verbose_name="Origin")),
                ("destination", models.BooleanField(verbose_name="Destination")),
                (
                    "cached_parent",
                    models.CharField(max_length=255, verbose_name="Parent"),
                ),
            ],
        ),
    ]
