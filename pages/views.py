from django.views.generic import TemplateView
from django.shortcuts import render
from pages.decorators import club_required, player_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from tournaments.models import Tournament
from participations.models import Participation

context = {'tournaments': Tournament.objects.all(), 'participations': Participation.objects.all()}

# @method_decorator(club_required, name='dispatch')
def HomePageView(request):
    return render(request, 'home.html')

def TournamentsView(request):
    return render(request, 'tournaments.html', context)