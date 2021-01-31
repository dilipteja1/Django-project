from django.db import models
# Create your models here.

class Job(models.Model):
    meta = models.CharField(max_length=100)
    apps = models.CharField(max_length=100)
    playlist = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=10 ,
                               choices=[{
                                'standard':'standard',
                                'debug':'debug'
                                }])
    sp  = models.CharField(max_length=20)
