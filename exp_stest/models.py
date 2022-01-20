from django.db import models

# Create your models here.

class SessionLogger(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    session_id = models.CharField(max_length=100)
    start_time_in_seconds = models.FloatField(null=True)
    end_time_in_seconds = models.FloatField(null=True)


    def __str__(self):
        return self.user_id + '-' + self.session_id + '-' + str(self.start_time_in_seconds) + '-' + str(self.end_time_in_seconds)
    

class STestScoreboard(models.Model):
    user_id = models.ForeignKey(SessionLogger, on_delete=models.CASCADE)
    stest_easy_num_question = models.IntegerField(default=0)
    stest_medium_num_question = models.IntegerField(default=0)
    stest_hard_num_question = models.IntegerField(default=0)
    stest_easy_score = models.FloatField(default=0) 
    stest_medium_score = models.FloatField(default=0)
    stest_hard_score = models.FloatField(default=0)
