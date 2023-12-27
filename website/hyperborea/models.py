from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Spell(models.Model):
    name = models.CharField(max_length=200, null=True, unique=True)
    description = models.TextField(null=True)
    saving_throw = models.CharField(max_length=2000, default="None", null=True)
    duration = models.CharField(max_length=200, null=True)
    range = models.CharField(max_length=200, null=True)
    page = models.PositiveIntegerField(validators=[MinValueValidator(175), MaxValueValidator(247)],null=True)
    magician_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)],null=True,default=0)
    cryomancer_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)],null=True,default=0)
    illusionist_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)],null=True,default=0)
    necromancer_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)],null=True,default=0)
    pyromancer_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)],null=True,default=0)
    witch_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)],null=True,default=0)
    cleric_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)],null=True,default=0)
    druid_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)],null=True,default=0)

    def __str__(self):
        return self.name
