from django.db import models
from users.models import CustomUser
from tournaments.models import Tournament
from django.utils import timezone
# Create your models here.
class Participation (models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date_joined = models.DateField(blank=True, default=timezone.now)
    handicap = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)
