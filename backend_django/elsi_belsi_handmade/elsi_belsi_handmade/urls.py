from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('elsi_belsi_handmade.elsi_belsi_auth.urls')),
    path('api/products/', include('elsi_belsi_handmade.elsi_belsi_products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
