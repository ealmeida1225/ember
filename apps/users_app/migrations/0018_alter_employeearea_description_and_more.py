# Generated by Django 4.2.1 on 2024-01-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users_app", "0017_alter_employeearea_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employeearea",
            name="description",
            field=models.TextField(max_length=256, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="employeeresponsability",
            name="description",
            field=models.TextField(max_length=256, verbose_name="description"),
        ),
    ]
