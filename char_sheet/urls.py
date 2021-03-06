from django.urls import path
from . import views
from .views import (CharactersListView,
    CharactersDetailView, CharactersCreateView, Character_itemsDetailView,
    ItemsCreateView, CharactersUpdateView, Item_enchantementsDeleteView,
    CharactersDeleteView, Character_itemsDeleteView, ItemsUpdateView,
    ItemsDeleteView, EnchantementsCreateView, EnchantementsUpdateView,
    EnchantementsDeleteView, Item_enchantementsCreateView, CICreateView,
    AbilitiesCreateView, AbilitiesUpdateView, AbilitiesDeleteView,
    Character_abilitiesCreateView, Character_abilitiesDeleteView,
    Character_abilitiesUpdateView, RaceCreateView, RaceUpdateView,
    Job_classCreateView, Job_classUpdateView, Job_classDeleteView,
    RaceDeleteView)

urlpatterns = [
    path('', CharactersListView.as_view(), name='char_sheet-home'),  # empty '' because homepage
    path('character/<pk>/', CharactersDetailView.as_view(), name='character-detail'),
    path('characters/new/', CharactersCreateView.as_view(), name='character-create'),
    path('character/<pk>/update/', CharactersUpdateView.as_view(), name='character-update'),
    path('character/<pk>/delete/', CharactersDeleteView.as_view(), name='character-delete'),
    path('character-items/<pk>', Character_itemsDetailView.as_view(), name='char_items-details'),
    path('character_items/delete/<pk>', Character_itemsDeleteView.as_view(), name='character_items-delete'),
    path('ci/new/<pk>', CICreateView.as_view(), name='ci-create'),
    path('Item_enchantements/new/<pk>', Item_enchantementsCreateView.as_view(), name='item_enchantements-create'),
    path('Item_enchantements/delete/<pk>', Item_enchantementsDeleteView.as_view(), name='item_enchantements-delete'),
    path('items/new/', ItemsCreateView.as_view(), name='items-create'),
    path('items/update/<pk>', ItemsUpdateView.as_view(), name='items-update'),
    path('items/delete/<pk>', ItemsDeleteView.as_view(), name='items-delete'),
    path('enchantements/new/', EnchantementsCreateView.as_view(), name='enchantements-create'),
    path('enchantements/update/<pk>', EnchantementsUpdateView.as_view(), name='enchantements-update'),
    path('enchantements/delete/<pk>', EnchantementsDeleteView.as_view(), name='enchantements-delete'),
    path('abilities/new/', AbilitiesCreateView.as_view(), name='abilities-create'),
    path('abilities/update/<pk>', AbilitiesUpdateView.as_view(), name='abilities-update'),
    path('abilities/delete/<pk>', AbilitiesDeleteView.as_view(), name='abilities-delete'),
    path('Character_abilities/new/<pk>', Character_abilitiesCreateView.as_view(), name='Character_abilities-create'),
    path('Character_abilities/update/<pk>', Character_abilitiesUpdateView.as_view(), name='Character_abilities-update'),
    path('Character_abilities/delete/<pk>', Character_abilitiesDeleteView.as_view(), name='Character_abilities-delete'),
    path('races/new', RaceCreateView.as_view(), name='race-create'),
    path('races/update/<pk>', RaceUpdateView.as_view(), name='race-update'),
    path('races/delete/<pk>', RaceDeleteView.as_view(), name='race-delete'),
    path('classes/new', Job_classCreateView.as_view(), name='job_class-create'),
    path('classes/update/<pk>', Job_classUpdateView.as_view(), name='job_class-update'),
    path('classes/delete/<pk>', Job_classDeleteView.as_view(), name='job_class-delete'),
    path('site/',views.site, name='char_sheet-site'),
    path('about/', views.about, name='char_sheet-about'),
    path('items/', views.items, name='char_sheet-items'),
    path('knows/<pk>', views.knows, name='char_sheet-knows'),
    path('carries/<int:pk>', views.carries, name='char_sheet-carries'),
    path('is_enchanted_with/<str:pk>', views.is_enchanted_with, name='char_sheet-is_enchanted_with'),
]
