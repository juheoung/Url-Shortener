from django.http import HttpResponseRedirect
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from urls.models import Urls
from urls.serializer import UrlsSerializer
import base62


class UrlsViewSet(viewsets.ModelViewSet):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer

    # def create(self, request, *args, **kwargs):
    #     respone = super().create(request, *args, **kwargs)
    #     show_url = f"{request.scheme}://{request.get_host()}/moveurl/{respone.data['sorturl']}"
    #     respone.data['sorturl'] = show_url
    #
    #     return respone

    def perform_create(self, serializer):
        last_id = Urls.objects.last()
        if last_id is None:
            user_id = 1
        else:
            user_id = last_id.id + 1

        user_id = base62.encode(user_id)

        change_url = f"{self.request.scheme}://{self.request.get_host()}/moveurl/{user_id}"

        if self.request.user.is_anonymous:
            user_name = None
        else:
            user_name = self.request.user

        serializer.save(
            owner=user_name,
            sorturl=user_id,
            changeurl=change_url,
        )


class MoveUrlsViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer
    lookup_field = 'sorturl'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        instance.counting += 1
        instance.save()
        return HttpResponseRedirect(serializer.data['url'])
