# Generated by Django 4.1.7 on 2023-04-22 04:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products_app", "0009_entity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="destination",
            name="name",
            field=models.CharField(max_length=30, unique=True, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="entity",
            name="name",
            field=models.CharField(max_length=30, unique=True, verbose_name="name"),
        ),
    ]