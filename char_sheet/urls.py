from django.urls import path
from . import views
from .views import CharactersListView, CharactersDetailView, CharactersCreateView

urlpatterns = [
    path('', CharactersListView.as_view(), name='char_sheet-home'),  # empty '' because homepage
    path('character/<pk>/', CharactersDetailView.as_view(), name='character-detail'),
    path('characters/new/', CharactersCreateView.as_view(), name='character-create'),
    path('site/',views.site, name='char_sheet-site'),
    path('about/', views.about, name='char_sheet-about'),
    path('items/', views.items, name='char_sheet-items'),
]
