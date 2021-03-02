from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('es_manager.urls')),
    path('accounts/', include('allauth.urls')),
]
