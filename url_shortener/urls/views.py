from rest_framework import viewsets
from urls.models import Urls
from urls.serializer import UrlsSerializer


class UrlsViewSet(viewsets.ModelViewSet):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer
