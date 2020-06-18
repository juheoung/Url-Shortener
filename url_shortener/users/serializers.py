from django.contrib.auth.models import User
from rest_framework import serializers
from urls.serializer import UrlsSerializer


class UserSerializer(serializers.ModelSerializer):

    owners = UrlsSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'owners',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(user.password)
        user.save()
        return user

