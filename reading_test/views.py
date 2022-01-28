from django.shortcuts import render
from rest_framework.decorators import api_view
from datetime import datetime
from .models import ReadingTestSessionLogger
from scoreboard.models import Scoreboard
from django.http import JsonResponse
from .reading_test_helper.reading_test_db import ReadingTestDB
from .reading_test_helper.reading_test_generator import ReadingTestGenerator
import os, json

current_dir = os.path.dirname(os.path.abspath(__file__))
test_db = json.load(open(os.path.join(current_dir, 'reading_test_db.json')))

@api_view(['POST'])
def test_session_logging(request):
    user_id = request.data['user_id']
    session_id = request.data['session_id']
    type = request.data['type']  # Start or Stop
    current_datetime_in_seconds = datetime.now().timestamp()
    status = 'Success'
    try:
        scoreboard, _ = Scoreboard.objects.get_or_create(user_id=user_id)
        session_logger, _ = ReadingTestSessionLogger.objects.get_or_create(user_id=scoreboard, session_id=session_id)
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
def generate_reading_tests(request):
    status = "Success"
    try:
        user_id = request.data['user_id']
        # Test if the user already has a reading test
        test = ReadingTestDB().retrieve_redis_db(user_id, 'Reading1')
        if test is not None:
            status = "Duplicated"
        else:
            test_ids = ReadingTestGenerator().generate_reading_test_ids()
            db = ReadingTestDB()
            for i, test_id in enumerate(test_ids):
                db.update_redis_db(user_id, f'Reading{i+1}', test_id)
    except Exception as e:
        status = "Error"
        print(e)
    return JsonResponse({'status': status})


@api_view(['POST'])
def get_reading_test(request):
    user_id = request.data['user_id']
    session_id = request.data['session_id']
    test_id = int(ReadingTestDB().retrieve_redis_db(user_id, session_id))
    return JsonResponse(test_db[test_id])


@api_view(['POST'])
def update_reading_test_score(request):
    status = 'Success'
    try:
        user_id = request.data['user_id']
        session_id = request.data['session_id']
        test_id = int(ReadingTestDB().retrieve_redis_db(user_id, session_id))
        number_of_correct_answers = request.data['number_of_correct_answers']
        total_questions = test_db[test_id]['num_questions']
        score = round(float(number_of_correct_answers) / float(total_questions) * 100, 2)
        obj, _ = Scoreboard.objects.get_or_create(user_id=user_id)

        if session_id == 'Reading1':
            obj.reading1_score = score
            obj.reading1_num_question = total_questions
        elif session_id == 'Reading2':
            obj.reading2_score = score
            obj.reading2_num_question = total_questions
        elif session_id == 'Reading3':
            obj.reading3_score = score
            obj.reading3_num_question = total_questions
        obj.save()

    except Exception as e:
        status = 'Error'
        print(e)
        
    return JsonResponse({'status': status})    

