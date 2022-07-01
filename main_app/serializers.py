from rest_framework import serializers
from main_app.models import Project, Bug, Comment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'project_description',
                  'project_technologies_used', 'project_status']


class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ['id', 'project_id',
                  'user_id',
                  'bug_name',
                  'bug_description',
                  'bug_status',
                  'bug_severity',
                  'bug_assignees', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id',
                  'user_id',
                  'project_id',
                  'bug_id',
                  'comment_text', ]
