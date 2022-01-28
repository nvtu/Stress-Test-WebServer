from django.urls import path, include
from . import views as local_views


urlpatterns = [
    path('test-session-logging', local_views.test_session_logging, name='test_session_logging'),
    path('generate-reading-tests', local_views.generate_reading_tests, name='generate_reading_tests'),
    path('get-reading-test', local_views.get_reading_test, name='get_reading_test'), 
    path('update-reading-test-score', local_views.update_reading_test_score, name='update_reading_test_score'),
]
