from rest_framework import serializers

from apps.todo.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'title', 'description', 'done', 'created_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
        }


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'title', 'done')
