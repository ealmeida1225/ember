# Generated by Django 4.1.7 on 2023-04-18 03:58

from django.db import migrations, transaction


@transaction.atomic
def create_clasifications(apps, schema_editor):
    Classification = apps.get_model("products_app", "Classification")
    Classification.objects.bulk_create(
        [
            Classification(name="Bebidas alcohólicas", description="Bebidas con alcohol"),
            Classification(name="Vinos", description=""),
            Classification(name="Refrescos", description="De cualquier sabor"),
            Classification(name="Vinagre", description="Industrial"),
        ]
    )


class Migration(migrations.Migration):
    dependencies = [
        ("products_app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_clasifications, migrations.RunPython.noop),
    ]