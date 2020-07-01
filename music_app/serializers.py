from rest_framework import serializers
from .models import Music, Album, Band, Member

class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Music
        fields = ('id','title', 'seconds', 'album')

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Album
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):

    class Meta:

        model = Band
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):

    class Meta:

        model = Member
        fields = '__all__'
