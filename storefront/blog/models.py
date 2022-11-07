from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.utils import timezone

class post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    author  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default = timezone.now)
    publish_date = models.DateTimeField(blank = True, null = True)
    
    def publish(self):
        self.publish_date = timezone.now
        self.save()
    
    def __str__(self) -> str:
        return self.title
         