from rest_framework import serializers
from .models import Artist, Song, Album, AlbumTrack

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title']

class AlbumTrackSerializer(serializers.ModelSerializer):
    song_title = serializers.ReadOnlyField(source='song.title')
    song_id = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.all(), source='song'
    )

    class Meta:
        model = AlbumTrack
        fields = ['id', 'song_id', 'song_title', 'track_number']

class AlbumSerializer(serializers.ModelSerializer):
    artist_name = serializers.ReadOnlyField(source='artist.name')
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(), source='artist'
    )
    tracks = AlbumTrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist_id', 'artist_name', 'release_year', 'cover', 'tracks']