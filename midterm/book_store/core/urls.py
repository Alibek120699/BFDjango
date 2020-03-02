from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, JournalViewSet, BookListCreateAPIView, JournalListCreateAPIView


urlpatterns = [
    path('books/', BookListCreateAPIView.as_view()),
    path('journals/', JournalListCreateAPIView.as_view()),
]

router = DefaultRouter()

router.register('books', BookViewSet, basename='books')
router.register('journals', JournalViewSet, basename='journal')
urlpatterns += router.urls
