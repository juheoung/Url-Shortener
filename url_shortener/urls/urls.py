from rest_framework import routers

from urls.views import UrlsViewSet

router = routers.SimpleRouter()
router.register('urls', UrlsViewSet)
urlpatterns = router.urls
