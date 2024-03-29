# Generated by Django 4.2.1 on 2023-06-25 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products_app", "0028_production_destination"),
    ]

    operations = [
        migrations.AddField(
            model_name="production",
            name="entity",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="products_app.entity",
                verbose_name="Entity",
            ),
        ),
    ]
