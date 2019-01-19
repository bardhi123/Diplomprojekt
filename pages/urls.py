from django.urls import path

from .views import HomePageView, TournamentsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tournaments', TournamentsView.as_view(), name='tournaments'),
]