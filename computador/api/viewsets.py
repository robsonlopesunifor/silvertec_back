from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import ListModelMixin
from computador.models import *
from .serializers import *

class ComputadorViewSet(ModelViewSet):
    queryset = Computador.objects.all()
    serializer_class = ComputadorSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwargs): #GET
        queryset = Computador.objects.filter(cliente__id=request.user.id)
        serializer = self.get_serializer(queryset,many=True)
        for computador in serializer.data:
            placa_mae = PlacaMae.objects.get(id=computador['placa_mae'])
            processador = Processador.objects.get(id=computador['processador'])
            placa_video = PlacaVideo.objects.get(id=computador['placa_video'])

            for m_ram in computador['memoria_ram']:
                memoria_ram = MemoriaRam.objects.get(id=m_ram[0])
                memoria_ram_serialisado = MemoriaRamSerializer(memoria_ram)
                m_ram[0] = memoria_ram_serialisado.data

            placa_mae_serialisado = PlacaMaeSerializer(placa_mae)
            processador_serialisado = ProcessadorSerializer(processador)
            placa_video_serialisado = PlacaVideoSerializer(placa_video)

            computador['placa_mae']   = placa_mae_serialisado.data
            computador['processador'] = processador_serialisado.data
            computador['placa_video'] = placa_video_serialisado.data
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        content = {
            'user': request.user,  # `django.contrib.auth.User` instance.
            'auth': request.auth,  # None
        }
        print(content)
        serializer = ComputadorSerializer(data=request.data)
        computador = Computador()
        if serializer.is_valid():      
            computador.placa_mae   = serializer.validated_data['placa_mae']
            computador.processador = serializer.validated_data['processador']
            computador.memoria_ram = serializer.validated_data['memoria_ram']
            computador.placa_video = serializer.validated_data['placa_video']
            computador.cliente = request.user
            computador.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlacaMaeViewSet(ModelViewSet):
    queryset = PlacaMae.objects.all()
    serializer_class = PlacaMaeSerializer

class MemoriaRamViewSet(ModelViewSet):
    queryset = MemoriaRam.objects.all()
    serializer_class = MemoriaRamSerializer

class PlacaVideoViewSet(ModelViewSet):
    queryset = PlacaVideo.objects.all()
    serializer_class = PlacaVideoSerializer

class ProcessadorViewSet(ModelViewSet):
    queryset = Processador.objects.all()
    serializer_class = ProcessadorSerializer
    