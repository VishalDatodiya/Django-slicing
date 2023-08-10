from django.db import models

class Result(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.FloatField(default=0)
    
    
    def __str__(self):
        return self.title
    
    
