from django.urls import include, path

from api.swagger.views import swagger_schema_view

from .routers import router


urlpatterns = [
    path('swagger/', swagger_schema_view, name='swagger-schema-ui'),

    path('', include(router.urls)),
]
