# Generated by Django 5.1.3 on 2024-11-21 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='male',
            name='girls',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.female'),
            preserve_default=False,
        ),
    ]