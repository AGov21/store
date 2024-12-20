from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import HomeTemplate

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include("products.urls", namespace="products")),
    path('', HomeTemplate.as_view(), name='home'),
    path('users/', include('users.urls', namespace='users'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)