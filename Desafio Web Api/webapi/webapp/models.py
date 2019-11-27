from django.db import models

# Create your models here.


class Contato(models.Model):

    class Meta:

        db_table = 'contato'

    nome = models.CharField(max_length=200)
    canal = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    obs = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome