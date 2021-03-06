from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from products import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include("products.urls", namespace='store')),
    path('about/', views.about, name="about"),
    path('', views.home, name="home"),
]
urlpatterns.extend(
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
)
urlpatterns.extend(
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   )