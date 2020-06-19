from django.contrib.auth.models import User
from model_bakery import baker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class UsersTestCase(APITestCase):
    def setUp(self) -> None:
        self.users = baker.make('auth.User', _quantity=3)

    def test_create(self):
        data = {'username': '1', 'password': '1'}
        response = self.client.post('/users/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(response.data['id'])
        self.assertEqual(response.data['username'], data['username'])

    def test_list(self):
        response = self.client.get('/users/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for user_response, user in zip(response.data['results'], self.users[::-1]):
            self.assertTrue(user_response['id'])
            self.assertEqual(user_response['username'], user.username)

    def test_detail(self):
        user = self.users[0]
        self.client.force_authenticate(user=user)
        response = self.client.get(f"/users/{user.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['id'])
        self.assertEqual(response.data['username'], user.username)

    def test_update(self):
        data = {'username': '1', 'password': '1'}
        user = self.users[0]
        self.client.force_authenticate(user=user)
        response = self.client.get(f"/users/{user.id}/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue(response.data['id'])
        self.assertEqual(response.data['username'], user.username)

    def test_delete(self):
        user = self.users[0]
        self.client.force_authenticate(user=user)
        response = self.client.delete(f"/users/{user.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.filter(id=user.id).exists())

    def test_login(self):
        user = User(
            username='1',
            password='1',
        )
        user.set_password(user.password)
        user.save()
        data = {
            'username': user.username,
            'password': '1'
        }
        response = self.client.post(f"/users/login/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['token'])

    def test_logout(self):
        user = User(
            username='1',
            password='1',
        )
        user.set_password(user.password)
        user.save()

        data = {
            'username': user.username,
            'password': '1',
        }
        response_login = self.client.post(f"/users/login/", data=data)

        token = response_login.data['token']
        response = self.client.delete(f"/users/logout/", HTTP_AUTHORIZATION='Token ' + token)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Token.objects.filter(key=token).exists())
