from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from videosbase.models import Trechos, Avaliacoes
from videosbase.api.serializers import TrechosSerializer, AvaliacoesSerializer

class TrechosViewSet(ModelViewSet):
    queryset = Trechos.objects.all()
    serializer_class = TrechosSerializer



class AvaliacoesViewSet(ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer

