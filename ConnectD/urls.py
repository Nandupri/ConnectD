from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
]

handler404 = 'jobs.views.custom_404_view'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
