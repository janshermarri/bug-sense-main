from django.contrib import admin
from main_app.models import Bug, Comments, Project
admin.site.register([Project, Bug, Comments])
