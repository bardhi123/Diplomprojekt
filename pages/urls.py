from django.urls import path

from .views import HomePageView, TournamentsView

urlpatterns = [
    path('', HomePageView, name='home'),
    path('tournaments/', TournamentsView, name='tournaments'),
]