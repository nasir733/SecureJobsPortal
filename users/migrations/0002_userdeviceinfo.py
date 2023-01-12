# Generated by Django 4.1.5 on 2023-01-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserDeviceInfo",
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
                ("user_ip", models.CharField(blank=True, max_length=155, null=True)),
                (
                    "device_type",
                    models.CharField(blank=True, max_length=155, null=True),
                ),
            ],
        ),
    ]
