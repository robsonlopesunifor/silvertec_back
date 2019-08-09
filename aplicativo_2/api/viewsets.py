from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from aplicativo_2.models import Musician, Album
from .serializers import MusicianSerializer, AlbumSerializer

class MusicianViewSet(ModelViewSet):
    
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

class AlbumViewSet(ModelViewSet):
    
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
