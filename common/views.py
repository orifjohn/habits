from django.shortcuts import render
from .models import Habit


# Create your views here.

def index_view(request):
    habits = Habit.objects.all()
    return render(request, 'main/index.html', {'habits': habits})


def good_habits(request):
    goods = Habit.objects.filter(is_good=False).all()
    return render(request, 'main/good.html', {'goods': goods})


def bad_habits(request):
    bads = Habit.objects.filter(is_good=True).all()
    return render(request, 'main/bad.html', {'bads': bads})
