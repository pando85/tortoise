from django.conf.urls import url, include

from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Tortoise API')

from .views import UserViewSet, TagViewSet, TaskViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'tags', TagViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    url(r'^token/$', views.obtain_auth_token),
    url(r'^', include(router.urls)),
    url(r'^$', schema_view)
]
