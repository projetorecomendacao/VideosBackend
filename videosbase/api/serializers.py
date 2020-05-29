from rest_framework.serializers import ModelSerializer
from videosbase.models import Trechos, Avaliacoes

class TrechosSerializer(ModelSerializer):
    class Meta:
        model = Trechos
        fields = '__all__'


class AvaliacoesSerializer(ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = '__all__'
