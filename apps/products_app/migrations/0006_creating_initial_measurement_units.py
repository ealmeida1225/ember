# Generated by Django 4.1.7 on 2023-04-19 05:05

from django.db import migrations, models, transaction


@transaction.atomic
def create_measurement_unit(apps, schema_editor):
    MeasurementUnit = apps.get_model("products_app", "MeasurementUnit")
    MeasurementUnit.objects.bulk_create(
        [
            MeasurementUnit(name="Mililitro", symbol="ml", description="0.001 litro", mililiters=1),
            MeasurementUnit(name="Centilitro", symbol="cl", description="0.01 litro", mililiters=10),
            MeasurementUnit(name="Decilitro", symbol="dl", description="0.1 litro", mililiters=100),
            MeasurementUnit(name="Litro", symbol="l", description="1 litro", mililiters=1000),
            MeasurementUnit(name="Decalitro", symbol="dal", description="10 litros", mililiters=10000),
            MeasurementUnit(name="Hectolitro", symbol="hl", description="100 litros", mililiters=100000),
            MeasurementUnit(name="Kilolitro", symbol="kl", description="1000 litros", mililiters=1000000),
        ]
    )


def reverse_function(apps, schema_editor):
    MeasurementUnit = apps.get_model("products_app", "MeasurementUnit")
    MeasurementUnit.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("products_app", "0005_measurementunit_and_more"),
    ]

    operations = [migrations.RunPython(create_measurement_unit, reverse_function)]