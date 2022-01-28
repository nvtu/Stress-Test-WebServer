from django.urls import path, include
from . import views as local_views


urlpatterns = [
    path('retrieve-scoreboard', local_views.retrieve_scoreboard, name='retrieve_scoreboard'),
]
