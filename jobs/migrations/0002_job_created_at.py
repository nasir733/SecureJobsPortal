# Generated by Django 3.2.4 on 2023-01-16 15:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 1, 16, 15, 23, 58, 980085, tzinfo=utc)),
            preserve_default=False,
        ),
    ]