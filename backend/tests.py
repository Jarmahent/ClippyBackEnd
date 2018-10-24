from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from rest_framework.test import RequestsClient
from rest_framework.authtoken.models import Token
from backend.serializers import CopyData
import json

# Useless tests


class TestEndPoints(APITestCase):
    def test_copy_data(self):
        client = RequestsClient()
        url = reverse('copydata')
        #client.credentials(HTTP_AUTHORIZATION='Token 294dde275500d23b490cfbfc5ee5040aedff808e')
        response = client.get('http://testserver/copydata/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_copyData_post(self):
        user = User.objects.create_user('username', 'Pas$w0rd')
        token = Token.objects.get(user__username='username')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post('/copydata/', json={
            'content': 'copy_data_here',
            'date': 'date',
            'user': '1'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("content", json.loads(response.content))
