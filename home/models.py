from django.db import models

#tabela Mensagem com tres colunas
class Mensagem(models.Model):
    titulo = modelos.CharField(max_length=120)
    conteudo = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True) #preenche a data

    class Meta:
        ordering = ["-criada_em"]

    def __str__(self):
        return self.titulo
