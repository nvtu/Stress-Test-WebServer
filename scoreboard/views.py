from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Scoreboard


# Create your views here.
@api_view(['GET'])
def retrieve_scoreboard(request):
    scoreboard_obj = Scoreboard.objects.all()
    scoreboard = []
    for score in scoreboard_obj:
        total_points = score.stest_easy_score + score.stest_medium_score + score.stest_hard_score + score.reading1_score + score.reading2_score + score.reading3_score
        scoreboard.append({
            'id': score.user_id,
            'STest_Easy': score.stest_easy_score,
            'STest_Medium': score.stest_medium_score,
            'STest_Hard': score.stest_hard_score,
            'Reading_1': score.reading1_score,
            'Reading_2': score.reading2_score,
            'Reading_3': score.reading3_score,
            'Points': total_points,
        })
    scoreboard = sorted(scoreboard, key=lambda k: k['Points'], reverse=True)
    for i, item in enumerate(scoreboard):
        item['rank'] = i + 1
    return JsonResponse(scoreboard, safe = False)