# Generated by Django 4.2.7 on 2023-12-26 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hyperborea', '0006_alter_characterclass_name_alter_spell_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spell',
            name='reversible',
        ),
    ]