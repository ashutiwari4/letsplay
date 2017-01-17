from rest_framework import routers
from views import SongList, GenreList

router = routers.SimpleRouter()
router.register(r'songs', SongList)
router.register(r'genre', GenreList)
