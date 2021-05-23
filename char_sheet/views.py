from django.shortcuts import render
from django.http import HttpResponse
from .models import (Items, Abilities, Race, Job_class, Information,
    Character_abilities, Enchantements, Item_enchantements)
from .models import Character_items as ci
from django.views.generic import (ListView, DetailView,
    DeleteView, CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def home(request):
    context = {
        'characters': Information.objects.all(),
    }
    return render(request, 'char_sheet/home.html', context)

class CharactersListView(ListView):
    model = Information
    template_name = 'char_sheet/home.html'
    context_object_name = 'characters'

class CharactersDetailView(DetailView):
    model = Information

class Character_itemsDetailView(DetailView):
    model = ci

class EnchantementsCreateView(LoginRequiredMixin, CreateView):
    model = Enchantements
    fields = ['enchantement_name', 'description', 'additional_damage']

    def form_valid(self, form):
        return super().form_valid(form)

class EnchantementsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Enchantements
    fields = ['description', 'additional_damage']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.username == 'admin':
            return True
        else:
            return False

class EnchantementsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Enchantements
    success_url = '/items/'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.username == 'admin':
            return True
        else:
            return False

class ItemsCreateView(LoginRequiredMixin, CreateView):
    model = Items
    fields = ['item_name', 'damage_points', 'special_ability', 'price']

    def form_valid(self, form):
        return super().form_valid(form)

class RaceCreateView(LoginRequiredMixin, CreateView):
    model = Race
    fields = ['race_name', 'description', 'special_ability']

    def form_valid(self, form):
        return super().form_valid(form)

class RaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Race
    fields = ['description', 'special_ability']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.username == 'admin':
            return True
        else:
            return False

class RaceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Race
    success_url = '/items/'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.username == 'admin':
            return True
        else:
            return False

class Job_classCreateView(LoginRequiredMixin, CreateView):
    model = Job_class
    fields = ['class_id', 'description', 'special_ability', 'weapon']

    def form_valid(self, form):
        return super().form_valid(form)


class Job_classUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job_class
    fields = ['description', 'special_ability', 'weapon']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.username == 'admin':
            return True
        else:
            return False

class Job_classDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job_class
    success_url = '/items/'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.username == 'admin':
            return True
        else:
            return False

class ItemsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Items
    fields = ['damage_points', 'special_ability', 'price']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.username == 'admin':
            return True
        else:
            return False

class ItemsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Items
    success_url = '/items/'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.username == 'admin':
            return True
        else:
            return False

class CharactersCreateView(LoginRequiredMixin, CreateView):
    model = Information
    fields = ['name', 'age', 'race', 'job_class', 'level', 'hit_points', 'magic_points', 'notes']

    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)

class CharactersDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Information
    success_url = '/profile/'

    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)

    def test_func(self):
        information = self.get_object()
        if self.request.user == information.player:
            return True
        else:
            return False


class CharactersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Information
    fields = ['name', 'age', 'level', 'hit_points', 'magic_points', 'notes']

    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)

    def test_func(self):
        information = self.get_object()
        if self.request.user == information.player:
            return True
        else:
            return False

class CICreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ci
    fields = ['item_name']

    def form_valid(self, form):
        form.instance.character_id = self.get_object().character_id
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if self.request.user.username == 'admin' or self.request.user == obj.character_id.player:
            return True
        else:
            return False

class Character_itemsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ci
    success_url = '/profile/'

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.character_id.player:
            return True
        else:
            return False

class Item_enchantementsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Item_enchantements
    fields = ['enchantement_name']

    def form_valid(self, form):
        #print(form.instance.item_name, self.get_object().item_name)
        form.instance.item_name = self.get_object().item_name
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if self.request.user.username == 'admin':
            return True
        else:
            return False

class Item_enchantementsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item_enchantements
    success_url = '/items/'

    def test_func(self):
        obj = self.get_object()
        if self.request.user.username == 'admin':
            return True
        else:
            return False


class AbilitiesCreateView(LoginRequiredMixin, CreateView):
    model = Abilities
    fields = ['ability_name', 'ability_description', 'ability_level', 'ability_is_magical', 'ability_score']

    def form_valid(self, form):
        return super().form_valid(form)

class AbilitiesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Abilities
    fields = ['ability_name', 'ability_description', 'ability_level', 'ability_is_magical', 'ability_score']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if self.request.user.username == 'admin':
            return True
        else:
            return False

class AbilitiesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Abilities
    success_url = '/items/'

    def test_func(self):
        obj = self.get_object()
        if self.request.user.username == 'admin':
            return True
        else:
            return False


class Character_abilitiesCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Character_abilities
    fields = ['abilities_id', 'additional_points']

    def form_valid(self, form):
        #print(form.instance.item_name, self.get_object().item_name)
        form.instance.information_id = self.get_object().information_id
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if self.request.user.username == 'admin' or self.request.user.username == obj.information_id.player.username:
            return True
        else:
            return False

class Character_abilitiesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Character_abilities
    fields = ['abilities_id', 'additional_points']

    def form_valid(self, form):
        #print(form.instance.item_name, self.get_object().item_name)
        form.instance.information_id = self.get_object().information_id
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if self.request.user.username == 'admin' or self.request.user.username == obj.information_id.player.username:
            return True
        else:
            return False

class Character_abilitiesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Character_abilities
    success_url = '/profile/'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if self.request.user.username == 'admin' or self.request.user.username == obj.information_id.player.username:
            return True
        else:
            return False

def about(request):
    return render(request, 'char_sheet/about.html', {'title': 'about'})

def site(request):
    return HttpResponse('<h1 style = "background-color:#ad5353; color:#360000; text-align:center">char_sheet site</h1>')

def items(request):
    context = {
        'items' : Items.objects.all(),
        'abilities': Abilities.objects.all(),
        'races': Race.objects.all(),
        'classes': Job_class.objects.all(),
        'enchantements': Enchantements.objects.all()
    }
    return render(request, 'char_sheet/items.html', context)

def carries(request, pk):
    if not ci.objects.filter(character_id=pk).exists():
        ci.objects.create(character_id=Information.objects.get(pk=pk), item_name=Items.objects.get(item_name='_'))
    context = {
        'query': ci.objects.filter(character_id=pk),
        'all': ci.objects.filter(character_id=pk).first(),
        'name': Information.objects.get(pk=pk),
    }

    return render(request, 'char_sheet/carries.html', context)

def is_enchanted_with(request, pk):
    if not Item_enchantements.objects.filter(item_name=pk).exists():
        Item_enchantements.objects.create(item_name=Items.objects.get(pk=pk), enchantement_name=Enchantements.objects.get(enchantement_name='_'))

    context = {
        'query': Item_enchantements.objects.filter(item_name=pk),
        'id': Item_enchantements.objects.filter(item_name=pk).first(),
        'item': Items.objects.get(pk=pk),
    }
    return render(request, 'char_sheet/is_enchanted_with.html', context)

def knows(request, pk):
    if not Character_abilities.objects.filter(information_id=pk).exists():
        Character_abilities.objects.create(information_id=Information.objects.get(pk=pk), abilities_id=Abilities.objects.get(ability_name='_'), additional_points=0)
    context = {
        'query': Character_abilities.objects.filter(information_id=pk),
        'all': Character_abilities.objects.filter(information_id=pk).first(),
        'name': Information.objects.get(pk=pk),
    }

    return render(request, 'char_sheet/knows.html', context)
