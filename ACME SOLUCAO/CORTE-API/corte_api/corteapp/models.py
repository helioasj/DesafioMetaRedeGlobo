from django.db import models

# Models
class Videos(models.Model):
    class Meta:
        db_table: 'videos'

    nome = models.CharField(max_length=100)
    path = models.CharField(max_length=200)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    duration = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100,null=True, blank=True,default='Pendente')

    def __str__(self):
        return self.nome + ' - ' + self.status_corte


