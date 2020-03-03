# Generated by Django 2.2.5 on 2019-11-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potd', '0004_auto_20191113_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='photooftheday',
            name='feature_potd',
            field=models.BooleanField(default=False, verbose_name='Featured POTD'),
        ),
        migrations.AddField(
            model_name='photooftheday',
            name='featured_as_potd',
            field=models.BooleanField(default=False, verbose_name='Has Been POTD'),
        ),
    ]
