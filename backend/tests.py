from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from backend.serializers import CopyData
from rest_framework.test import RequestsClient
from json import dumps


# Useless tests


class TestEndPoints(APITestCase):
    def test_copy_data(self):
        client = RequestsClient()
        url = reverse('copydata')
        #client.credentials(HTTP_AUTHORIZATION='Token 294dde275500d23b490cfbfc5ee5040aedff808e')
        response = client.get('http://testserver/copydata/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_copyData_post(self):
        client = RequestsClient()
        user = User.objects.all().filter(username='admin')

        response = client.post('http://testserver/copydata/', json={
            'content': 'MegaCorp',
            'date': 'datehere',
            'user': 1
        }, headers={'Authorization': 'Token 294dde275500d23b490cfbfc5ee5040aedff808e'})
        force_authenticate(response, user=user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
