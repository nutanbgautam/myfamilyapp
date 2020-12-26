"""

MyFamilyApp URL Configuration

"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/',admin.site.urls),
    path('',include('MyFamilyApp.frontend.urls',namespace="frontend")),
    path('app/',include('MyFamilyApp.backend.urls',namespace="backend"))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns+=[path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)