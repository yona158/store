# Generated by Django 5.1.3 on 2024-11-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
