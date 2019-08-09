from django.contrib import admin
from .models import PlacaMae, Processador, MemoriaRam, PlacaVideo, Computador


# Register your models here.
    
admin.site.register(PlacaMae)
admin.site.register(Processador)
admin.site.register(MemoriaRam)
admin.site.register(PlacaVideo)
admin.site.register(Computador)