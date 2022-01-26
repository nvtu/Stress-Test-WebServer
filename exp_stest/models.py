from django.db import models

# Create your models here.

class STestScoreboard(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100, default='')
    stest_easy_num_question = models.IntegerField(default=0)
    stest_medium_num_question = models.IntegerField(default=0)
    stest_hard_num_question = models.IntegerField(default=0)
    stest_easy_score = models.FloatField(default=0) 
    stest_medium_score = models.FloatField(default=0)
    stest_hard_score = models.FloatField(default=0)


class SessionLogger(models.Model):
    user_id = models.ForeignKey(STestScoreboard, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=100, default='')
    start_time_in_seconds = models.FloatField(null=True)
    end_time_in_seconds = models.FloatField(null=True)


