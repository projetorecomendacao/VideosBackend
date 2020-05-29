from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

from videosbase.api.viewsets import TrechosViewSet, AvaliacoesViewSet

router = routers.DefaultRouter()

router.register(r'trechos',TrechosViewSet,basename='Trechos')
router.register(r'avaliacoes',AvaliacoesViewSet,basename='Avaliações')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
