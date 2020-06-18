from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class UsersTestCase(APITestCase):
    def setUp(self):
        self.users = User(username='1', password='1')
        self.users.set_password(self.users.password)

    def test_list(self):
        user = self.users
        self.client.force_authenticate(user=user)
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.fail()

    # def test_create(self):
    #     data = {
    #         'username': '1',
    #         'password': '1',
    #     }
    #     response = self.client.post('/users/', data=data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    #     print(response.data['password'])
    #
    #     self.assertTrue(response.data['id'])
    #     self.assertEqual(response.data['username'], data['username'])
    #
    #     self.fail()

    def test_update(self):
        pass

    def test_detail(self):
        pass

    def test_delete(self):
        pass
