# Generated by Django 4.2.1 on 2023-06-29 03:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users_app", "0015_alter_systememail_historical_vault_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="systemuser",
            name="photo",
            field=models.ImageField(
                null=True, upload_to="images/", verbose_name="photo"
            ),
        ),
    ]
