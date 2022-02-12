from django.urls import path, include
from . import views as local_views


urlpatterns = [
    path('session-logging', local_views.session_logging, name='session_logging'),
]
