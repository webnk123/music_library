from django.urls import include, path
from rest_framework import routers
from app import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# swagger documentation schema
schema_view = get_schema_view(
   openapi.Info(
      title="artists api",
      default_version='v 0.1',
      description="api for CRUD operations on artists, albums and songs, has 4 non generic views. 1. for getting all songs in an album 2. to get all albums by author 3/4. to add / remove existing song from an album (with serial number)",
      terms_of_service="None",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'songs', views.SongViewSet)


urlpatterns = [
   
   path('', include(router.urls)),

   path('songs/by/<str:album>', views.SongsByAlbum.as_view()),
   path('albums/by/<int:artist>', views.AlbumsByArtist.as_view()),

   path('RemoveFromAlbum/album/<int:alb_id>/song/<int:sng_id>', views.RemoveFromAlbum),
#   path('AddToAlbum/album/<int:alb_id>/song/<int:sng_id>/order/<int:order>', views.AddToAlbum),
   path('AddToAlbum/',  views.AddToAlbum.as_view()),

   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]