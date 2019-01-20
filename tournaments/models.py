from django.db import models
from users.models import CustomUser
from django.utils import timezone


def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)

# Create your models here.
class Tournament(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    tourn_date = models.DateTimeField(blank=True, default=one_day_hence())
    def __str__(self):
        """A string representation of the model."""
        return self.name