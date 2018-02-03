from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TagViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tags', TagViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
