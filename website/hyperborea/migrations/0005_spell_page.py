# Generated by Django 4.2.7 on 2023-12-26 18:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyperborea', '0004_spell_reversible'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='page',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(175), django.core.validators.MaxValueValidator(247)]),
        ),
    ]
