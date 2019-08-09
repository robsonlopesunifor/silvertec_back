from django.contrib import admin
from django.conf.urls import include
from django.urls import path
#-------------------------------------------------
from rest_framework import routers #REST
from aplicativo_1.api.viewsets import PersonViewSet
from aplicativo_2.api.viewsets import MusicianViewSet, AlbumViewSet
from computador.api.viewsets import *
from cadastro.api.viewsets import cadastrarUsuario
from rest_framework.authtoken.views import obtain_auth_token
#-----------------------------
from django.conf import settings


router = routers.DefaultRouter() #REST
router.register(r'person', PersonViewSet, base_name='Person')
router.register(r'musician', MusicianViewSet, base_name='Musician') #rest
router.register(r'album', AlbumViewSet, base_name='Album') #rest
router.register(r'computador', ComputadorViewSet, base_name='Computador') #rest
router.register(r'placa_mae', PlacaMaeViewSet, base_name='Placa Mae') #rest
router.register(r'memoria_ram', MemoriaRamViewSet, base_name='Memoria Ram') #rest
router.register(r'processador', ProcessadorViewSet, base_name='Processador') #rest
router.register(r'placa_video', PlacaVideoViewSet, base_name='Placa video') #rest


urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('cadastro/cadastrar/', cadastrarUsuario,name='cadastrar usuario'),
    path('api-token-auth/', obtain_auth_token)
]