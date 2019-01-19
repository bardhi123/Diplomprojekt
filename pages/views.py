from django.views.generic import TemplateView
from pages.decorators import club_required, player_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# @method_decorator(club_required, name='dispatch')
class HomePageView(TemplateView):
    template_name = 'home.html'

class TournamentsView(TemplateView):
    template_name = 'tournaments.html'