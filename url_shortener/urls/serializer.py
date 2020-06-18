from rest_framework import serializers
from urls.models import Urls


class UrlsSerializer(serializers.ModelSerializer):

    sorturl = serializers.ReadOnlyField()

    class Meta:
        model = Urls
        fields = (
            'id',
            'url',
            'sorturl',
        )
