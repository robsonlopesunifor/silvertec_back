from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class PlacaMae(models.Model):
    produto = models.CharField(max_length=100)
    processador = models.CharField(max_length=50)
    quantidade_slots = models.IntegerField()
    quantidade_memoria = models.IntegerField()
    video_integrado = models.BooleanField(default=True)


    def __str__(self):
        return self.produto

class Processador(models.Model):
    produto = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)


    def __str__(self):
        return self.produto

class MemoriaRam(models.Model):
    produto = models.CharField(max_length=100)
    tamanho = models.IntegerField()

    def __str__(self):
        return str(self.tamanho)


class PlacaVideo(models.Model):
    produto = models.CharField(max_length=100)

    def __str__(self):
        return self.produto


class Computador(models.Model):
    placa_mae = models.ForeignKey(PlacaMae, on_delete=models.CASCADE)
    processador = models.ForeignKey(Processador, on_delete=models.CASCADE)
    memoria_ram = ArrayField(ArrayField(models.IntegerField(),size=2) )
    placa_video = models.ForeignKey(PlacaVideo, on_delete=models.CASCADE,blank=True, null=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.placa_mae.produto