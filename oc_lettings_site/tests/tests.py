from django import test
import pytest
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse


class TestView:
    @classmethod
    def setup(cls):
        cls.user_test = User.objects.create_user(username='username', password='password')
        cls.profile = Profile.objects.create(
            user=cls.user_test,
            favorite_city='favorite_city',
        )

        cls.client_test = test.Client()

    @pytest.mark.django_db
    def test_index(self):
        url = reverse('profiles:index')
        response = self.client_test.get(url)
        assert response.status_code == 200
        assert '<title>Profiles</title>' in response.content.decode()

    @pytest.mark.django_db
    def test_profile_view(self):
        url = reverse('profiles:profile', args=[self.user_test.username])
        response = self.client_test.get(url)
        assert response.status_code == 200
        assert '<title>username</title>' in response.content.decode()
