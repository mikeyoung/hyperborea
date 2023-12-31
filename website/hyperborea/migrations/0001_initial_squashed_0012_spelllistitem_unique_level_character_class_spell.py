# Generated by Django 4.2.7 on 2023-12-29 20:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('hyperborea', '0001_initial'), ('hyperborea', '0002_alter_characterclass_name'), ('hyperborea', '0003_alter_spell_saving_throw'), ('hyperborea', '0004_spell_reversible'), ('hyperborea', '0005_spell_page'), ('hyperborea', '0006_alter_characterclass_name_alter_spell_name'), ('hyperborea', '0007_remove_spell_reversible'), ('hyperborea', '0008_characterclass_spelllistitem'), ('hyperborea', '0009_remove_spelllistitem_character_class_and_more'), ('hyperborea', '0010_spell_cleric_level_spell_cryomancer_level_and_more'), ('hyperborea', '0011_characterclass_remove_spell_cleric_level_and_more'), ('hyperborea', '0012_spelllistitem_unique_level_character_class_spell')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
                ('description', models.TextField(null=True)),
                ('saving_throw', models.CharField(default='None', max_length=2000, null=True)),
                ('duration', models.CharField(max_length=200, null=True)),
                ('range', models.CharField(max_length=200, null=True)),
                ('page', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(175), django.core.validators.MaxValueValidator(247)])),
            ],
        ),
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpellListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('character_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='character_class_spell_list_item', to='hyperborea.characterclass')),
                ('spell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spell_spell_list_item', to='hyperborea.spell')),
            ],
        ),
        migrations.AddConstraint(
            model_name='spelllistitem',
            constraint=models.UniqueConstraint(fields=('level', 'character_class', 'spell'), name='unique_level_character_class_spell'),
        ),
    ]
