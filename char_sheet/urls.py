from django.urls import path
from . import views
from .views import (CharactersListView,
    CharactersDetailView, CharactersCreateView, Character_itemsDetailView,
    ItemsCreateView, Character_itemsCreateView, CharactersUpdateView,
    CharactersDeleteView, Character_itemsDeleteView)

urlpatterns = [
    path('', CharactersListView.as_view(), name='char_sheet-home'),  # empty '' because homepage
    path('character/<pk>/', CharactersDetailView.as_view(), name='character-detail'),
    path('characters/new/', CharactersCreateView.as_view(), name='character-create'),
    path('character/<pk>/update/', CharactersUpdateView.as_view(), name='character-update'),
    path('character/<pk>/delete/', CharactersDeleteView.as_view(), name='character-delete'),
    path('character-items/<pk>', Character_itemsDetailView.as_view(), name='char_items-details'),
    path('character-items/<pk>', Character_itemsDetailView.as_view(), name='char_items-details'),
    path('character_items/delete/<pk>', Character_itemsDeleteView.as_view(), name='character_items-delete'),    
    path('character_items/new/<pk>', Character_itemsCreateView.as_view(), name='character_items-create'),
    path('items/new/', ItemsCreateView.as_view(), name='items-create'),
    path('site/',views.site, name='char_sheet-site'),
    path('about/', views.about, name='char_sheet-about'),
    path('items/', views.items, name='char_sheet-items'),
    path('carries/<int:pk>', views.carries, name='char_sheet-carries'),
]
