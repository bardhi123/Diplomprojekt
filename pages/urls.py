from django.urls import path

from .views import home, TournamentDetailView, TournamentListView, TournamentCreateView, TournamentUpdateView, TournamentDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('tournaments/', TournamentListView.as_view(), name='tournaments'),
    path('tournaments/new/', TournamentCreateView.as_view(), name='tournament_create'),
    path('tournaments/<int:pk>/', TournamentDetailView.as_view(), name='tournament_detail'),
    path('tournaments/<int:pk>/update', TournamentUpdateView.as_view(), name='tournament_update'),
    path('tournaments/<int:pk>/delete', TournamentDeleteView.as_view(), name='tournament_delete'),
]