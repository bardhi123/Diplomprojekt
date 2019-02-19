from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from tournaments.algorithm import invoke_algorithm

from .views import (home,
                    profile,
                    TournamentDetailView,
                    TournamentListView,
                    TournamentCreateView,
                    TournamentUpdateView,
                    TournamentDeleteView,
                    TournamentParticipantsView,
                    ParticipationCreateView,
                    ParticipationDeleteView,
                    ParticipationUpdateView)

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('tournaments/', TournamentListView.as_view(), name='tournaments'),
    path('tournaments/new/', TournamentCreateView.as_view(), name='tournament_create'),
    path('tournaments/<int:pk>/', TournamentDetailView.as_view(), name='tournament_detail'),
    path('tournaments/<int:pk>/update', TournamentUpdateView.as_view(), name='tournament_update'),
    path('tournaments/<int:pk>/delete', TournamentDeleteView.as_view(), name='tournament_delete'),
    path('tournaments/<int:pk>/participants', TournamentParticipantsView.as_view(), name='tournament_participants'),
    path('tournaments/<int:pk>/participate', ParticipationCreateView.as_view(), name='participation_form'),
    path('tournaments/<int:pk>/quit', ParticipationDeleteView.as_view(), name='participation_delete'),
    path('tournaments/<int:pk>/changeHC', ParticipationUpdateView.as_view(), name='participation_update'),
]

#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

# call the algorithm at startup for testing purposes
response = invoke_algorithm(None, True)
print(response)
