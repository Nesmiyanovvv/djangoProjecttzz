from django.db import models

# Create your models here.


class Memory(models.Model):
    location = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)