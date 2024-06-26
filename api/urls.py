from django.urls import path, include
from rest_framework import routers
from api import views
from django.conf import settings
from django.conf.urls.static import static
router = routers.DefaultRouter()
router.register(r'datos', views.DatosViewSet)

urlpatterns = [
    path('', include(router.urls))
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)