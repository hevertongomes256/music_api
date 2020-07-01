from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from music_app import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Musics List API",
        default_version='v1',
        description="An api for Musicss",
        terms_of_service="https://heverton/terms/",
        contact=openapi.Contact(email="music@music.remote"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Routers usados para criação de funcionalidades com viewsets

#router.register(r'musics', views.MusicList)
#router.register(r'bands', views.BandViewSet)
#router.register(r'albums', views.AlbumViewSet)
#router.register(r'members', views.MemberViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', schema_view.with_ui('swagger', 
                                    cache_timeout=0), name='schema-swagger-ui'),
    path("redoc", schema_view.with_ui('redoc',
                                    cache_timeout=0), name='schema-redoc'),


    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    path('admin/', admin.site.urls),

    path('musics/', views.MusicList.as_view()),
    path('musics/<int:pk>', views.MusicDetail.as_view()),

    path('bands/', views.BandList.as_view()),
    path('bands/<int:pk>', views.BandDetail.as_view()),

    path('albums/', views.AlbumList.as_view()),
    path('albums/<int:pk>', views.AlbumDetail.as_view()),

    path('members/', views.MemberList.as_view()),
    path('members/<int>', views.MemberDetail.as_view()),

]
