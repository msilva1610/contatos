from django.db import models
from django.utils import timezone
# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=200)
    mail = models.EmailField()
    mensagem = models.TextField()
    datapublicacao = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.datapublicacao = timezone.now()
    def __str__(self):
        return self.nome
