from django.db import models

class Trechos (models.Model):
    video_endereco = models.CharField(max_length=100)
    inicio = models.IntegerField()
    fim = models.IntegerField()

    def __str__(self):
        return 'ID: ' + str(self.pk) + '  Vídeo: ' + self.video_endereco + '  Inicio: ' + str(self.inicio) + '  Fim: ' + str(self.fim) 


class Avaliacoes (models.Model):
    nome = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=60, null=True)
    trecho_id = models.IntegerField(null=True)
    resposta = models.CharField(max_length=1)
    data_avaliacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "nome: " + self.nome + "   Trecho: " + str(self.trecho_id) + "  Resposta: " + self.resposta
