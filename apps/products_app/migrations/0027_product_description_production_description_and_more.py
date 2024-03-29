# Generated by Django 4.2.1 on 2023-05-31 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products_app", "0026_alter_groupingpackaging_historical_vault_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="description"),
        ),
        migrations.AddField(
            model_name="production",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="description"),
        ),
        migrations.AlterField(
            model_name="product",
            name="classification",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="products_app.classification",
            ),
            preserve_default=False,
        ),
    ]
