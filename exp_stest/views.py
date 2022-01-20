from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from .stest_helper.stest_generator import STestGenerator
from .stest_helper.stest_validator import STestValidator
from .stest_helper.stest_db import STestDB
from datetime import datetime
from .models import SessionLogger, STestScoreboard


# Create your views here.
@api_view(['POST'])
def test_session_logging(request):
    user_id = request.data['user_id']
    session_id = request.data['session_id']
    type = request.data['type'] # Start or Stop
    current_datetime_in_seconds = datetime.now().timestamp()    
    status = 'Success'
    try: 
        session_logger, _ = SessionLogger.objects.get_or_create(user_id=user_id, session_id=session_id)
        if type == 'Start':
            session_logger.start_time_in_seconds = current_datetime_in_seconds
        else:
            session_logger.end_time_in_seconds = current_datetime_in_seconds
        session_logger.save()
    except Exception as e:
        status = 'Error'
        print(e)
    return JsonResponse({'status': status})


@api_view(['POST'])
def generate_stest_with_level(request):
    user_id = request.data['user_id']
    level = request.data['level']
    formula, answer = STestGenerator(level).generate_stest()
    STestDB().update_redis_db(user_id, formula, answer)
    response = {
        'level': level,
        'formula': formula,
    }
    return JsonResponse(response)


@api_view(['POST'])
def validate_answer(request):
    user_id = request.data['user_id']
    level = request.data['level']
    answer = int(request.data['answer'])
    validate_result = STestValidator().validate(user_id, answer)

    if validate_result:
        obj = STestScoreboard.objects.get(user_id=user_id)
        if level == 'Easy':
            obj.stest_easy_num_question += 1
            obj.stest_easy_score += 1
        elif level == 'Medium':
            obj.stest_medium_num_question += 1
            obj.stest_medium_score += 2
        elif level == 'Hard':
            obj.stest_hard_num_question += 1
            obj.stest_hard_score += 3
        obj.save()

    response = { 'validate_result': validate_result }
    return JsonResponse(response)