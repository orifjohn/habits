from django.shortcuts import render
from .models import Habit


# Create your views here.

def index_view(request):
    habit = Habit.objects.all()
    return render(request, 'index.html', {'habit': habit})
