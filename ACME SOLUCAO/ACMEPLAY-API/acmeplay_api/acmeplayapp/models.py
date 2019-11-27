from django.db import models

# Models
class Acmeplay(models.Model):
    class Meta:
        db_table: 'acmeplay'

    titulo = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)
    nome_arquivo = models.CharField(max_length=200)


    def __str__(self):
        return self.titulo + ' - ' + self.duracao + ' - ' + self.nome_arquivo