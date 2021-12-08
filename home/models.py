from django.db import models

# Create your models here.



class session(models.Model):
    sessionId =models.CharField(max_length=225)