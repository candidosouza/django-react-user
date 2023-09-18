from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.urls import urlpatterns as users_urls


schema_view = get_schema_view(
   openapi.Info(
      title="Py Users Api",
      default_version='v1',
      description="Py Users Api",
      terms_of_service="#",
      contact=openapi.Contact(email="candidosouzza@gmail.com"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('user-platform-admin/', admin.site.urls),
    path('', include(users_urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('schema<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
