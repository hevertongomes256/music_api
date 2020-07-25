from django.urls import path
from .views import (
    MusicList,
    MusicDetail,
    AlbumList,
    AlbumDetail,
    BandList,
    BandDetail,
    MemberList,
    MemberDetail
)

urlpatterns = [
    
    path('musics/', MusicList.as_view()),
    path('musics/<int:pk>', MusicDetail.as_view()),

    path('bands/', BandList.as_view()),
    path('bands/<int:pk>', BandDetail.as_view()),

    path('albums/', AlbumList.as_view()),
    path('albums/<int:pk>', AlbumDetail.as_view()),
    path('albums/<int:album_pk>/musics', MusicList.as_view(), name='music_album'),


    path('members/', MemberList.as_view()),
    path('members/<int:pk>', MemberDetail.as_view()),
]
