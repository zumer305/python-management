from rest_framework import serializers
from .models import Task
from projects.models import Project
from datetime import date


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_at', 'is_completed']

    #  VALIDATION
    def validate(self, data):

        due_date = data.get('due_date')
        project = data.get('project')

        # 1. due date check
        if due_date and due_date < date.today():
            raise serializers.ValidationError("Due date cannot be in the past")

        # 2. project ownership check
        request = self.context.get('request')

        if project and request:
            if project.created_by != request.user:
                raise serializers.ValidationError("You cannot create task in another user's project")

        return data