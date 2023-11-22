from django.db import models

# verification/models.py
from django.db import models

class SerialKey(models.Model):
    key = models.CharField(max_length=20, unique=True)
    used_time = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.key
