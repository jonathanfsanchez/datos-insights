# Generated by Django 2.1.7 on 2019-02-16 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='cost',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='title',
            field=models.TextField(),
        ),
    ]