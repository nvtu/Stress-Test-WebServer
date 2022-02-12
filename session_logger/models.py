from django.db import models

# Create your models here.

class SessionLogger(models.Model):
    user_id = models.CharField(max_length=100, default='')
    session_id = models.CharField(max_length=100, default='')
    start_time_in_seconds = models.FloatField(null=True)
    end_time_in_seconds = models.FloatField(null=True)