from django.db import models
from datetime import datetime

# Create your models here.
class trivia(models.Model):
    question = models.CharField(max_length=200)
    body = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = "Trivia"
#class posts(models.Model):
#    title = models.CharField(max_length=200)
#    body = models.TextField()
#    created_at = models.DateTimeField(default=datetime.now, blank=True)
