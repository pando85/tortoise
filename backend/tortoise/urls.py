from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('tortoise.api.urls', namespace='api')),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
