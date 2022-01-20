from django.urls import path, include
from . import views as local_views


urlpatterns = [
    path('test-session-logging', local_views.test_session_logging, name='test_session_logging'),
    path('generate-stest-with-level', local_views.generate_stest_with_level, name='generate_stest_with_level'),
    path('validate-answer', local_views.validate_answer, name='validate_answer'),
]
