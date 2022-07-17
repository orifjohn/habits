from django.urls import path, include
from .views import index_view, good_habits, bad_habits

urlpatterns = [
    path("", index_view, name='index-url'),
    path("good/", good_habits, name='good_habits_url'),
    path("bad/", bad_habits, name='bad_habits_url')
]
