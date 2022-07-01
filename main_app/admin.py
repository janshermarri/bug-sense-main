from django.contrib import admin
from main_app.models import Bug, Comment, Project
admin.site.register([Project, Bug, Comment])
