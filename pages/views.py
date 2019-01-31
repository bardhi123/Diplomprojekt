from django.views.generic import TemplateView
from django.shortcuts import render
from pages.decorators import club_required, player_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DeleteView, CreateView, DetailView, UpdateView
from tournaments.models import Tournament
from participations.models import Participation
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#context = {'tournaments': Tournament.objects.all().order_by('-tourn_date'), 'participations': Participation.objects.all()}

# @method_decorator(club_required, name='dispatch')
def home(request):
    return render(request, 'home.html')

class TournamentListView(LoginRequiredMixin, ListView):
    template_name = 'tournaments.html'
    context_object_name = 'tournaments'

    def get_queryset(self):
        return Tournament.objects.all().order_by('-tourn_date')

    def get_context_data(self, **kwargs):
        context = super(TournamentListView, self).get_context_data(**kwargs)
        context['participations'] = Participation.objects.all()
        return context

class TournamentDetailView(LoginRequiredMixin, DetailView):
    model = Tournament
    template_name = 'tournament_detail.html'

class TournamentCreateView(LoginRequiredMixin, CreateView):
    model = Tournament
    template_name = 'tournament_form.html'
    fields = ['name', 'description', 'tourn_date']
    """"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)"""

class TournamentUpdateView(LoginRequiredMixin, UpdateView): #(LoginRequiredMixin, UserPassesTestMixin, UpdateView)
    model = Tournament
    template_name = 'tournament_update.html'
    fields = ['name', 'description', 'tourn_date']

    """
    def test_func(self):
        tournament = self.get_object()
        if self.request.user == tournament.author:
            return True
        return False"""

class TournamentDeleteView(LoginRequiredMixin, DeleteView):
    model = Tournament
    template_name = 'tournament_confirm_delete.html'
    success_url = '/tournaments'
    """
        def test_func(self):
            tournament = self.get_object()
            if self.request.user == tournament.author:
                return True
            return False"""