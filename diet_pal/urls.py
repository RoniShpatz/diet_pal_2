from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
# Use static() to add URL mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diet_log/', include('diet_log.urls')),
    path('', RedirectView.as_view(url='diet_log/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)