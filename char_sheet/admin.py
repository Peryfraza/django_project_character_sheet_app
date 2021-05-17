from django.contrib import admin
from .models import (Items, Abilities, Race,
    Job_class, Information, Character_items,
    Character_abilities, Enchantements, Item_enchantements)

# Register your models here.
admin.site.register(Items)
admin.site.register(Abilities)
admin.site.register(Race)
admin.site.register(Job_class)
admin.site.register(Information)
admin.site.register(Character_items)
admin.site.register(Character_abilities)
admin.site.register(Enchantements)
admin.site.register(Item_enchantements)
