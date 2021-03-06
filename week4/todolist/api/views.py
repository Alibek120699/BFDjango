# from django.contrib.auth.decorators import permission_required
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return TaskSerializer


class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return TaskSerializer
