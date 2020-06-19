from rest_framework import serializers
from urls.models import Urls


class UrlsSerializer(serializers.ModelSerializer):
    counting = serializers.ReadOnlyField()
    changeurl = serializers.ReadOnlyField()

    class Meta:
        model = Urls
        fields = (
            'id',
            'url',
            'counting',
            'changeurl',
        )
