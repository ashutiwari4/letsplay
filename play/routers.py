from rest_framework import routers
from views import SongList, GenreList, SongDetails

router = routers.SimpleRouter()
router.register(r'songs', SongList)
router.register(r'genre', GenreList)
router.register(r'song_details', SongDetails)
