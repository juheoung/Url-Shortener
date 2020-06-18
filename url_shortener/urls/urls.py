from rest_framework import routers

from urls.views import UrlsViewSet, MoveUrlsViewSet

router = routers.SimpleRouter()
router.register('urls', UrlsViewSet)
router.register('moveurl', MoveUrlsViewSet)
urlpatterns = router.urls
