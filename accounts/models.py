from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    batch_name = models.CharField(max_length=100, blank=True)
    is_trainer = models.BooleanField(default=False)

    def __str__(self):
        return self.username
