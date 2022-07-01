from django.db import models
from django.contrib.auth.models import User

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


class Bug(models.Model):
    SEVERITY_CHOICES = [
        ('NORMAL', 'Normal'),
        ('URGENT', 'Urgent'),
        ('LAZY', 'Lazy'),
    ]

    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bug_name = models.CharField(max_length=1024)
    bug_description = models.TextField(blank=True, max_length=2048)
    bug_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    bug_severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    bug_assignees = models.CharField(max_length=1024)

    def __str__(self):
        return self.bug_name + " " + self.user_id + " " + self.project_id


class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    bug_id = models.ForeignKey(Bug, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=True, max_length=2048)

    def __str__(self):
        return self.user_id + '-' + self.comment_text + '-' + self.bug_id
