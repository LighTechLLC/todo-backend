from drf_yasg import openapi
from drf_yasg.views import get_schema_view


swagger_schema_view = get_schema_view(
    openapi.Info(title='To Do', default_version='v1'),
    public=True,
).with_ui('swagger')
