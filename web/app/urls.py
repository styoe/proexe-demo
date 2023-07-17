from django.conf import settings
# from django.contrib import admin
from django.urls import path, include
from .api.urls import urlpatterns as api_urls

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/', include(api_urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns 
