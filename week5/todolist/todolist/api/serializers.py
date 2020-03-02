from rest_framework import serializers

from .models import Task
from todolist.todolist.users import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email')


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)

    def create(self, validated_data):
        new_task = Task(**validated_data)
        new_task.save()
        return new_task

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance
