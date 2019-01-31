from django.urls import path, include
from rest_framework import routers

from app.api.todo_view_set import TodoViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'todos', TodoViewSet, basename='todo')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1/', include(router.urls))
]
