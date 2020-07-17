from rest_framework import viewsets, generics
from django_filters import rest_framework as filters
from .models import Music, Album, Band, Member
from .serializers import MusicSerializer, BandSerializer, AlbumSerializer, MemberSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all().select_related('album')
    serializer_class = MusicSerializer
    ## Autenticação Básica: Apenas usuários logados acessam a url
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    # Implementação de filtros
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['title']


class MusicDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['title']

class BandList(generics.ListCreateAPIView):

    queryset = Band.objects.all()
    serializer_class = BandSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class BandDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Band.objects.all()
    serializer_class = BandSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

## Filtro customisado para range de datas

class AlbumFilter(filters.FilterSet):

    date_age = filters.DateFilter(field_name='date', lookup_expr='gte')
    date_lte = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:

        model = Album
        fields = '__all__'

class AlbumList(generics.ListCreateAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['title', 'date', 'band']
    filter_class = AlbumFilter

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Album.objects.all().select_related('band')
    serializer_class = AlbumSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['title', 'date', 'band']

class MemberList(generics.ListCreateAPIView):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['name', 'age', 'band']

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Member.objects.all().select_related('band')
    serializer_class = MemberSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['name', 'age', 'band']
