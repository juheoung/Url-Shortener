from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from urls.models import Urls


class UrlsSerializer(ModelSerializer):

    sorturl = serializers.URLField(read_only=True)

    class Meta:
        model = Urls
        fields = (
            'url',
            'sorturl',
        )