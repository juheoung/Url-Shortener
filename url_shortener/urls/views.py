from django.http import HttpResponseRedirect
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from urls.models import Urls
from urls.serializer import UrlsSerializer
import base62


class UrlsViewSet(viewsets.ModelViewSet):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer

    def create(self, request, *args, **kwargs):
        respone = super().create(request, *args, **kwargs)
        show_url = f"{request.scheme}://{request.get_host()}/moveurl/{respone.data['sorturl']}"
        respone.data['sorturl'] = show_url
        return respone

    def perform_create(self, serializer):
        a = Urls.objects.last()
        if a is None:
            b = 1
        else:
            b = a.id + 1

        b = base62.encode(b)
        serializer.save(
            sorturl=b,
            owner=self.request.user
        )


class MoveUrlsViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer
    lookup_field = 'sorturl'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return HttpResponseRedirect(serializer.data['url'])
