from django.db import models
from scoreboard.models import Scoreboard

# Create your models here.

class ReadingTestSessionLogger(models.Model):
    user_id = models.ForeignKey(Scoreboard, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=100, default='')
    start_time_in_seconds = models.FloatField(null=True)
    end_time_in_seconds = models.FloatField(null=True)