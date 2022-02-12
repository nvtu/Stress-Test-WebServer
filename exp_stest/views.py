from rest_framework.decorators import api_view
from django.http import JsonResponse

from .stest_helper.stest_generator import STestGenerator
from .stest_helper.stest_validator import STestValidator
from .stest_helper.stest_db import STestDB
from datetime import datetime
from .models import STestSessionLogger
from scoreboard.models import Scoreboard


# Create your views here.
@api_view(['POST'])
def reset_score(request):
    user_id = request.data['user_id']
    session_id = request.data['session_id']
    level = session_id.split('_')[-1] 
    status = 'Success'
    try: 
        scoreboard, _ = Scoreboard.objects.get_or_create(user_id=user_id)
        # Reset the scoreboard for the new session corresponding to the level
        if level == 'Easy':
            scoreboard.stest_easy_num_question = 0
            scoreboard.stest_easy_num_correct = 0
        elif level == 'Medium':
            scoreboard.stest_medium_num_question = 0
            scoreboard.stest_medium_num_correct = 0
        elif level == 'Hard':
            scoreboard.stest_hard_num_question = 0
            scoreboard.stest_hard_num_correct = 0
        scoreboard.save()
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
    try:
        answer = int(request.data['answer'])
        validate_result = STestValidator().validate(user_id, answer)
    except:
        validate_result = False

    obj, _ = Scoreboard.objects.get_or_create(user_id=user_id)
    if level == 'Easy':
        obj.stest_easy_num_question += 1
        if validate_result:
            obj.stest_easy_num_correct += 1
    elif level == 'Medium':
        obj.stest_medium_num_question += 1
        if validate_result:
            obj.stest_medium_num_correct += 1
    elif level == 'Hard':
        obj.stest_hard_num_question += 1
        if validate_result:
            obj.stest_hard_num_correct += 1
    obj.save()

    response = { 'validate_result': validate_result }
    return JsonResponse(response)