from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CourseListCreateAPIView, CourseViewSet


urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view()),
]

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')

urlpatterns += router.urls
