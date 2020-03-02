from django.urls import path

from .views import task_list, task_list_detail


urlpatterns = [
    path('fbv/tasks/', task_list),
    path('fbv/tasks/<int:pk>/', task_list_detail),
]
