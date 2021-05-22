from django.urls import path
from . import views
from .views import (CharactersListView,
    CharactersDetailView, CharactersCreateView, Character_itemsDetailView,
    ItemsCreateView, CharactersUpdateView, Item_enchantementsDeleteView,
    CharactersDeleteView, Character_itemsDeleteView, ItemsUpdateView,
    ItemsDeleteView, EnchantementsCreateView, EnchantementsUpdateView,
    EnchantementsDeleteView, Item_enchantementsCreateView, CICreateView)

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
    path('site/',views.site, name='char_sheet-site'),
    path('about/', views.about, name='char_sheet-about'),
    path('items/', views.items, name='char_sheet-items'),
    path('carries/<int:pk>', views.carries, name='char_sheet-carries'),
    path('is_enchanted_with/<str:pk>', views.is_enchanted_with, name='char_sheet-is_enchanted_with'),
]
