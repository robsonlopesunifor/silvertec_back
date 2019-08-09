from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError


@api_view(['POST'])
def cadastrarUsuario(request):
    try:
        usuario_email = User.objects.get(email=request.data['campo-email'])
        usuario_username = User.objects.get(username=request.data['campo-nome-usuario'])

        if usuario_email or usuario_username:
            raise ValidationError('Erro! Já existe um usuário com o mesmo e-mail ou mesmo username')

    except User.DoesNotExist:
        nome_usuario = request.data['campo-nome-usuario']
        email = request.data['campo-email']
        senha = request.data['campo-senha']

        novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        novoUsuario.save()
        token = Token.objects.get(user__username=nome_usuario)
        return Response({'Token':token.key})

