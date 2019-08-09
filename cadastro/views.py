from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

@csrf_protect
@require_POST
def cadastrar_usuario(request):
    try:
        usuario_email = User.objects.get(email=request.POST['campo-email'])
        usuario_username = User.objects.get(email=request.POST['campo-nome-usuario'])

        if usuario_email or usuario_username:
            return render(request, 'caminho para o index', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail ou mesmo username'})

    except User.DoesNotExist:
        nome_usuario = request.POST['campo-nome-usuario']
        email = request.POST['campo-email']
        senha = request.POST['campo-senha']

        novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        novoUsuario.save()

@require_POST
def entrar(request):
    usuario_aux = User.objects.get(email=request.POST['email'])
    usuario = authenticate(username=usuario_aux.username,
                           password=request.POST["senha"])
    if usuario is not None:
        login(request, usuario)
        return HttpResponseRedirect('/home/')

    return HttpResponseRedirect('/')

@login_required
def sair(request):
    logout(request)
    return HttpResponseRedirect('/')

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/home/")
    else:
        return render(request, "caminho para index.html")