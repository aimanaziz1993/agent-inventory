from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponse('200 Welcome to REST API Interface: Agent-Inventory'), name='home'),
    # API V1
    path('api/v1/', include(([

        path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),

        path('user/', include('users.urls')),
        path('profile/', include('profiles.urls')),
        path('blog/', include('blog_api.urls')),
        path('inventory/', include('inventory_api.urls')),

    ], 'api'), namespace='api-v1')),

    path('api-auth/', include('rest_framework.urls')),
    path('docs', include_docs_urls(title='Agent-Inventory API')),
    path('schema', get_schema_view(
        title="Agent-Inventory API",
        description="",
        version="1.0.1",
    ), name='schema')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
