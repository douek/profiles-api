import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .api.serializers import ProfileSerializer, ProfileStatusSerializer
from .models import Profile, ProfileStatus

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {'username': 'test1',
                'email': 'lol@test.com',
                'password1': 'strong_pass_123',
                'password2': 'strong_pass_123'}
        response = self.client.post('/api/rest-auth/registration/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):

    list_url = reverse('profile-list')

    def setUp(self):
        self.user = User.objects.create_user(username='test2',password='strong_pass_123')

        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrive(self):
        response = self.client.get(reverse('profile-detail',kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'test2')

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse('profile-detail',kwargs={'pk': 1}),
        {'city' : 'RaananCity',
        'bio': 'updated bio' })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {'id': 1,
        'user': 'test2',
        'bio': 'updated bio',
        'city':'RaananCity',
        'avatar': None})

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user('random',password='strong_pass_123')
        self.client.force_authenticate(random_user)
        response = self.client.put(reverse('profile-detail',kwargs={'pk': 1}),
        {'city' : 'BLA BLA BLA',
        'bio': 'Hacked!!' })

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ProfileStatusViewSetTestCase(APITestCase):

    list_url = reverse('status-list')

    def setUp(self):
        self.user = User.objects.create_user(username='test2',password='strong_pass_123')
        self.status = ProfileStatus.objects.create(user_profile=self.user.profile,
            status_content='hahaha test' )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_status_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_status_create(self):
        data = {'status_content': 'hahaha new status'}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user_profile'], 'test2')
        self.assertEqual(response.data['status_content'], 'hahaha new status')

    def test_single_status_retrive(self):
        serializer_data = ProfileStatusSerializer(instance=self.status).data
        response = self.client.get(reverse('status-detail',kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_status_update_owner(self):
        data = {'status_content': 'hahaha update status'}
        response = self.client.put(reverse('status-detail',kwargs={'pk':1}),
        data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status_content'], 'hahaha update status')

    def test_status_update_random_user(self):
        random_user = User.objects.create_user('random',password='strong_pass_123')
        self.client.force_authenticate(random_user)
        data = {'status_content': 'hahaha you been hacked'}
        response = self.client.put(reverse('status-detail',kwargs={'pk':1}),
        data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)