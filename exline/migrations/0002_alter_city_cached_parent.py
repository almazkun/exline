# Generated by Django 3.2 on 2021-04-21 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exline", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="cached_parent",
            field=models.CharField(max_length=255, null=True, verbose_name="Parent"),
        ),
    ]