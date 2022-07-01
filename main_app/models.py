from django.db import models

STATUS_CHOICES = [
    ('TODO', 'To Do'),
    ('DOING', 'Doing'),
    ('IN_REVIEW', 'In Review'),
    ('DONE', 'Done')
]


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField(blank=True, max_length=1500)
    project_technologies_used = models.TextField(blank=True, max_length=1000)
    project_status = models.CharField(max_length=9, choices=STATUS_CHOICES)

    def __str__(self):
        return self.project_name + ' ' + self.project_status

