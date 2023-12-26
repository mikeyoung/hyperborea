from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Spell(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    saving_throw = models.CharField(max_length=2000, default="None", null=True)
    duration = models.CharField(max_length=200, null=True)
    range = models.CharField(max_length=200, null=True)
    reversible = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name

class CharacterClass(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class SpellListItem(models.Model):
    level = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)],null=True)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE, related_name="character_class_spell_list_item", null=True)
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE, related_name="spell_spell_list_item", null=True)

    def __str__(self):
        return f"{self.character_class} {self.level} {self.spell.name}" 