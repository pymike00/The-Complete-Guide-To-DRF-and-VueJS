import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer
from profiles.models import Profile, ProfileStatus


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"username": "testcase", "email": "test@localhost.app",
                "password1": "some_strong_psw", "password2": "some_strong_psw"}
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ProfileViewSetTestCase(APITestCase):

    list_url = reverse("profile-list")

    def setUp(self):
        self.user = User.objects.create_user(username="davinci",
                                             password="some-very-strong-psw")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse("profile-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], "davinci")

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
                                   {"city": "Anchiano", "bio": "Renaissance Genius"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                         {"id": 1, "user": "davinci", "bio": "Renaissance Genius",
                          "city": "Anchiano", "avatar": None})

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user(username="random", 
                                               password="psw123123123")
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse("profile-detail", kwargs={"pk": 1}),
                                   {"bio": "hacked!!!"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ProfileStatusViewSetTestCase(APITestCase):

    url = reverse("status-list")

    def setUp(self):
        self.user = User.objects.create_user(username="davinci",
                                             password="some-very-strong-psw")
        self.status = ProfileStatus.objects.create(user_profile=self.user.profile,
                                                   status_content="status test")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_status_list_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_status_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_status_create(self):
        data = {"status_content": "a new status!"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user_profile"], "davinci")
        self.assertEqual(response.data["status_content"], "a new status!")

    def test_single_status_retrieve(self):
        serializer_data = ProfileStatusSerializer(instance=self.status).data
        response = self.client.get(reverse("status-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_status_update_owner(self):
        data = {"status_content": "content updated"}
        response = self.client.put(reverse("status-detail", kwargs={"pk": 1}),
                                   data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status_content"], "content updated")

    def test_status_update_random_user(self):
        random_user = User.objects.create_user(username="random", 
                                               password="psw123123123")
        self.client.force_authenticate(user=random_user)
        data = {"status_content": "You Have Been Hacked!"}
        response = self.client.put(reverse("status-detail", kwargs={"pk": 1}),
                                   data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
