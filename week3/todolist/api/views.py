from rest_framework import generics

class Task(generics.ListCreateAPIView):
    serializer_class = TaskSerializer