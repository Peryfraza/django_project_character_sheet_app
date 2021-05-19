from django.shortcuts import render
from django.http import HttpResponse
from .models import Items, Abilities, Race, Job_class, Information, Character_items, Character_abilities, Enchantements, Item_enchantements
from django.views.generic import ListView, DetailView, CreateView
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

class CharactersCreateView(CreateView):
    model = Information
    fields = ['name', 'age', 'race', 'job_class', 'level', 'hit_points', 'magic_points']

    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'char_sheet/about.html', {'title': 'about'})

def site(request):
    return HttpResponse('<h1 style = "background-color:#ad5353; color:#360000; text-align:center">char_sheet site</h1>')
