from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter


from .views import RegisterMyUserAPIView, MyUserViewSet


urlpatterns = [
    path('auth/login/', obtain_jwt_token),
    path('auth/register/', RegisterMyUserAPIView.as_view()),
]

router = DefaultRouter()
router.register('users', MyUserViewSet, basename='users')

urlpatterns += router.urls
