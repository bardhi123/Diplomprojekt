from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    is_staff = models.BooleanField(default=False)
    # add additional fields in here

    def __str__(self):
        return self.email