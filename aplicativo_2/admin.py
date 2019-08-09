from django.contrib import admin
from .models import Musician, Album


# Register your models here.
class MusicianAdmin(admin.ModelAdmin):
    pass

class AlbumAdmin(admin.ModelAdmin):
    pass

admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)