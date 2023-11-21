from django.db import models

# verification/models.py
from django.db import models

class SerialKey(models.Model):
    key = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.key
