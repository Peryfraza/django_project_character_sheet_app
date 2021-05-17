from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Items(models.Model):
    item_name = models.CharField(max_length=100, primary_key=True)
    damage_points = models.IntegerField(blank=True, null=True)
    special_ability = models.CharField(max_length=250, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.item_name +' ( '+'dmg = '+str(self.damage_points)+' )'

class Abilities(models.Model):
    ability_name = models.CharField(max_length=30)
    ability_description = models.CharField(max_length=250, blank=True, null=True)
    ability_level = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(50), MinValueValidator(0)]
    )
    ability_is_magical = models.BooleanField(default=False)
    ability_score = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(50), MinValueValidator(0)]
    )

    def __str__(self):
        is_mag = 'non-magical'
        if self.ability_is_magical:
            is_mag = 'magical'
        return self.ability_name+ ' ' + is_mag


class Race(models.Model):
    RACE_NAMES = (
        ('HUMAN', 'Human'),
        ('DWARF', 'Dwarf'),
        ('ELF', 'Elf'),
        ('HALF_ELF', 'Half-Elf'),
        ('HALFLING', 'Halfling'),
        ('TIEFLING', 'Tiefling')
    )
    race_name = models.CharField(max_length=30, choices=RACE_NAMES, primary_key=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    special_ability = models.ForeignKey(Abilities, on_delete=models.CASCADE)

    def __str__(self):
        strin = self.race_name
        strin1 = strin[0]
        strin2 = strin[1:]
        strin = strin1+strin2.lower()
        return strin

class Job_class(models.Model):
    JOB_CLASS_NAMES = (
        ('HUNTER', 'Hunter'),
        ('ASSASSIN', 'Assassin'),
        ('THIEF', 'Thief'),
        ('PALADIN', 'Paladin'),
        ('DRUID', 'Druid'),
        ('WIZARD', 'Wizard'),
        ('NONE', 'None')
    )
    class_id = models.CharField(max_length=30, choices=JOB_CLASS_NAMES, primary_key=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    weapon = models.ForeignKey(Items, on_delete=models.CASCADE)
    special_ability = models.ForeignKey(Abilities, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        strin = self.class_id
        strin1 = strin[0]
        strin2 = strin[1:]
        strin = strin1+strin2.lower()
        return strin

class Information(models.Model):
    player = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    job_class = models.ForeignKey(Job_class, on_delete=models.CASCADE)
    level = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    hit_points = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(50), MinValueValidator(0)]
    )
    magic_points = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(50), MinValueValidator(0)]
    )
    notes = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return 'player: ' + str(player) + self.name+" the " + str(self.race) + ' ' + str(self.job_class) + ' ( ' + str(self.age) + ' )'

    def get_absolute_url(self):
        return reverse('character-detail', kwargs={'pk': self.pk})

class Character_items(models.Model):
    item_name = models.ForeignKey(Items, on_delete=models.CASCADE)
    character_id = models.ForeignKey(Information, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.character_id) + ' carries ' + str(self.item_name)

class Character_abilities(models.Model):
    information_id = models.ForeignKey(Information, on_delete=models.CASCADE)
    abilities_id = models.ForeignKey(Abilities, on_delete=models.CASCADE)
    additional_points = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(50), MinValueValidator(0)]
    )

    def __str__(self):
        return str(self.information_id) + ' uses ' + str(self.abilities_id)

class Enchantements(models.Model):
    enchantement_name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    additional_damage = models.IntegerField(
        default = 0,
        validators=[MaxValueValidator(30), MinValueValidator(-30)]
    )
    def __str__(self):
         add = '+'
         if self.additional_damage < 0:
             add = ''
         return self.enchantement_name + ' ( ' + add + str(self.additional_damage) + ' )'

class Item_enchantements(models.Model):
    item_name = models.ForeignKey(Items, on_delete=models.CASCADE)
    enchantement_name = models.ForeignKey(Enchantements, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item_name) + ' - ' + str(self.enchantement_name)
