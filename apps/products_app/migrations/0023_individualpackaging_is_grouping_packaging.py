# Generated by Django 4.1.7 on 2023-05-05 22:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products_app", "0022_format_product_format"),
    ]

    operations = [
        migrations.AddField(
            model_name="individualpackaging",
            name="is_grouping_packaging",
            field=models.BooleanField(
                default=False, verbose_name="is grouping packaging"
            ),
        ),
    ]
