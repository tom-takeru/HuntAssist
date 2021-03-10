from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include

from . import settings_common, settings_dev

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('es_manager.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)