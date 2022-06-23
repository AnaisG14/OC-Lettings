from django import test
from django.urls import reverse


class TestView:

    def test_index(self):
        url = reverse('index')
        client_test = test.Client()
        response = client_test.get(url)
        assert response.status_code == 200
        assert '<title>Holiday Homes</title>' in response.content.decode()
