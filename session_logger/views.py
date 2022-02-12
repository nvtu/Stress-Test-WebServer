from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import SessionLogger
from datetime import datetime
from scoreboard.models import Scoreboard

# Create your views here.

@api_view(['POST'])
def session_logging(request):
    user_id = request.data['user_id']
    session_id = request.data['session_id']
    type = request.data['type']  # Start or Stop
    current_datetime_in_seconds = datetime.now().timestamp()
    status = 'Success'
    try:
        scoreboard, _ = Scoreboard.objects.get_or_create(user_id=user_id)
        session_logger, _ = SessionLogger.objects.get_or_create(user_id=user_id, session_id=session_id)
        if type == 'Start':
            session_logger.start_time_in_seconds = current_datetime_in_seconds
        else:
            session_logger.end_time_in_seconds = current_datetime_in_seconds
        session_logger.save()
    except Exception as e:
        status = 'Error'
        print(e)

    return JsonResponse({'status': status, 'log_time': current_datetime_in_seconds})