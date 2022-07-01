from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=1500)
    technologies_used = models.TextField(blank=True, max_length=1000)