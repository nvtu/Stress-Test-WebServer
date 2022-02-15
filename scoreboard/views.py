from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Scoreboard


# Create your views here.
@api_view(['GET'])
def retrieve_scoreboard(request):
    STEST_EASY_SCORE_PER_QUESTION = 1
    STEST_MEDIUM_SCORE_PER_QUESTION = 2
    STEST_HARD_SCORE_PER_QUESTION = 3

    scoreboard_obj = Scoreboard.objects.all()
    scoreboard = []
    for score in scoreboard_obj:
        total_points = score.reading1_score + score.reading2_score + score.reading3_score
        stest_easy_score = max(0, (3 * score.stest_easy_num_correct - score.stest_easy_num_question) / 2 * STEST_EASY_SCORE_PER_QUESTION)
        stest_medium_score = max(0, (3 * score.stest_medium_num_correct - score.stest_medium_num_question) / 2 * STEST_MEDIUM_SCORE_PER_QUESTION)
        # print(score.stest_medium_num_correct, score.stest_medium_num_question)
        stest_hard_score = max(0, (3 * score.stest_hard_num_correct - score.stest_hard_num_question) / 2 * STEST_HARD_SCORE_PER_QUESTION)
        total_points += stest_easy_score + stest_medium_score + stest_hard_score
        scoreboard.append({
            'id': score.user_id,
            'STest_Easy': stest_easy_score,
            'STest_Medium': stest_medium_score,
            'STest_Hard': stest_hard_score,
            'Reading_1': score.reading1_score,
            'Reading_2': score.reading2_score,
            'Reading_3': score.reading3_score,
            'Points': total_points,
        })
    scoreboard = sorted(scoreboard, key=lambda k: k['Points'], reverse=True)
    for i, item in enumerate(scoreboard):
        item['rank'] = i + 1
    return JsonResponse(scoreboard, safe = False)