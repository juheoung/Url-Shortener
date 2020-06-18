from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from rest_framework.response import Response
from users.pagination import CustomPagination
from users.permission import IsOwnerOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = CustomPagination

    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
        # username = request.POST['username']
        # password = request.POST['password']
        # user = autten

    @action(methods=['delete'], detail=False)
    def logout(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

