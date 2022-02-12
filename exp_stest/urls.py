from django.urls import path, include
from . import views as local_views


urlpatterns = [
    path('reset-score', local_views.reset_score, name='reset_score'),
    path('generate-stest-with-level', local_views.generate_stest_with_level, name='generate_stest_with_level'),
    path('validate-answer', local_views.validate_answer, name='validate_answer'),
]
