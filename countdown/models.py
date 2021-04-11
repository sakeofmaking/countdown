# countdown/models.py
from django.db import models


class Counter(models.Model):
    start_msg = models.TextField()
    end_msg = models.TextField()
    count_to = models.CharField(max_length=100)

    def __str__(self):
        return self.start_msg[:50]
