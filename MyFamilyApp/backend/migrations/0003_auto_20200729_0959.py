# Generated by Django 3.0.8 on 2020-07-29 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200727_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profession',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='remarks',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
