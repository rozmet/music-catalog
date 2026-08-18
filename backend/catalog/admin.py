from django.contrib import admin
from .models import Artist, Song, Album, AlbumTrack

class AlbumTrackInline(admin.TabularInline):
    model = AlbumTrack
    extra = 1

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_year')
    inlines = [AlbumTrackInline]

admin.site.register(Artist)
admin.site.register(Song)