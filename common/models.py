from django.db import models
from helpers.models import BaseModel


# Create your models here.

class Habit(BaseModel):
    title = models.CharField(max_length=128, unique=True, verbose_name="Nomi")
    is_good = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
