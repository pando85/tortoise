from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, TagViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'tag', TagViewSet)
router.register(r'task', TaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
