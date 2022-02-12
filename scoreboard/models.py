from django.db import models

# Create your models here.

class Scoreboard(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100, default='')
    stest_easy_num_question = models.IntegerField(default=0)
    stest_medium_num_question = models.IntegerField(default=0)
    stest_hard_num_question = models.IntegerField(default=0)
    stest_easy_num_correct = models.FloatField(default=0) 
    stest_medium_num_correct = models.FloatField(default=0)
    stest_hard_num_correct = models.FloatField(default=0)
    reading1_num_question = models.IntegerField(default=0)
    reading2_num_question = models.IntegerField(default=0)
    reading3_num_question = models.IntegerField(default=0)
    reading1_score = models.FloatField(default=0) 
    reading2_score = models.FloatField(default=0)
    reading3_score = models.FloatField(default=0)