from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from videosbase.models import Trechos, Avaliacoes
from videosbase.api.serializers import TrechosSerializer, AvaliacoesSerializer



class TrechosViewSet(ModelViewSet):
    
    query = Trechos.objects.all() #retorna todos os objetos que estão cadastrados no banco

    assuntos = query.values_list('video_assunto', flat=True).distinct() #retorna todos os assuntos que estão cadastrados no banco
    assuntos = [u for u in assuntos]
    
    id_list = []
    for assunto in assuntos:
        trechos_assunto = query.filter(video_assunto=assunto)
        id_trecho_aleatorio = trechos_assunto.random().values_list('id', flat=True)[0]
        id_list.append(id_trecho_aleatorio)  

    queryset = Trechos.objects.filter(id__in=id_list)
    serializer_class = TrechosSerializer



class AvaliacoesViewSet(ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer


