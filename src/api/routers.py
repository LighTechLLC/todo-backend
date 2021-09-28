from rest_framework.routers import DefaultRouter

from .views import ToDoViewSet


router = DefaultRouter()
router.register('todo', ToDoViewSet)
