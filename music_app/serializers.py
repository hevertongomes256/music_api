from rest_framework import serializers
from .models import Music, Album, Band, Member


class BandSerializer(serializers.ModelSerializer):

    class Meta:

        model = Band
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Album
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Music
        fields = ('id','title', 'seconds', 'album')


class MemberSerializer(serializers.ModelSerializer):

    class Meta:

        model = Member
        fields = '__all__'