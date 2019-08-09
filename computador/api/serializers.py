from rest_framework.serializers import ModelSerializer
from computador.models import PlacaMae, Processador, MemoriaRam, PlacaVideo, Computador
from django.core.exceptions import ValidationError


class ComputadorSerializer(ModelSerializer):
    class Meta:
        model = Computador
        fields = '__all__'
        read_only_fields = ('cliente',)

    def validate(self, data):
        total_de_memoria = 0
        total_de_slots = 0

        for valor in data['memoria_ram']:
            try:
                memoria_ram = MemoriaRam.objects.get(id=valor[0])
                total_de_memoria += memoria_ram.tamanho * valor[1]
                total_de_slots += valor[1]
            except MemoriaRam.DoesNotExist:
                raise ValidationError('Memoria RAM não existe.')
            
        if data['placa_mae'].processador != data['processador'].marca:
            raise ValidationError('Processador não compativel com a placa.')
        elif data['placa_mae'].video_integrado == False and data['placa_video'] == None:
            raise ValidationError('Placa mãe necessita de placa de video.')
        elif data['placa_mae'].quantidade_slots < total_de_slots:
            raise ValidationError('Numero de memorias RAM esta acima do numero de slots da placa mãe.')
        elif data['placa_mae'].quantidade_memoria < total_de_memoria:
            raise ValidationError('Total de GB da memorias RAM esta acima do suportado pela placa mãe.')
        return data

class PlacaMaeSerializer(ModelSerializer):
    class Meta:
        model = PlacaMae
        fields = '__all__'

class ProcessadorSerializer(ModelSerializer):
    class Meta:
        model = Processador
        fields = '__all__'

class MemoriaRamSerializer(ModelSerializer):
    class Meta:
        model = MemoriaRam
        fields = '__all__'

class PlacaVideoSerializer(ModelSerializer):
    class Meta:
        model = PlacaVideo
        fields = '__all__'
