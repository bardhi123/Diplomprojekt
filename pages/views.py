from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from pages.decorators import club_required, player_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DeleteView, CreateView, DetailView, UpdateView
from tournaments.models import Tournament
from participations.models import Participation
from users.models import CustomUser
from users.forms import CustomUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#context = {'tournaments': Tournament.objects.all().order_by('-tourn_date'), 'participations': Participation.objects.all()}

# @method_decorator(club_required, name='dispatch')
def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = CustomUserChangeForm(instance=request.user)
    context = { 'u_form': u_form}
    return render(request, 'account/profile.html', context)

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
    template_name = 'tournament_detail.html'
    context_object_name = 'tournaments'

    def get_queryset(self):
        return Tournament.objects.all().order_by('-tourn_date')

    def get_context_data(self, **kwargs):
        context = super(TournamentDetailView, self).get_context_data(**kwargs)
        context['participations'] = Participation.objects.filter(tournament=self.kwargs.get('pk'), player=self.request.user)
        return context

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

class TournamentParticipantsView(LoginRequiredMixin, ListView):
    template_name = 'tournament_participants.html'
    context_object_name = 'users'

    def get_queryset(self):
        return CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TournamentParticipantsView, self).get_context_data(**kwargs)
        context['participations'] = Participation.objects.filter(tournament=self.kwargs.get('pk'))
        return context

class ParticipationCreateView(LoginRequiredMixin, CreateView):
    model = Participation
    template_name = 'participation_form.html'
    fields = ['handicap']
    success_url = '/tournaments'

    def form_valid(self, form):
        tour = Tournament.objects.filter(id=self.kwargs.get('pk'))
        form.instance.player = self.request.user
        form.instance.tournament = tour.first()
        return super().form_valid(form)

class ParticipationUpdateView(LoginRequiredMixin, UpdateView): #(LoginRequiredMixin, UserPassesTestMixin, UpdateView)
    model = Participation
    template_name = 'participation_update.html'
    fields = ['handicap']
    success_url = '/tournaments'

class ParticipationDeleteView(LoginRequiredMixin, DeleteView):
    model = Participation
    template_name = 'participation_delete.html'
    success_url = '/tournaments'