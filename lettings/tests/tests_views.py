from django import test
import pytest
from lettings.models import Letting, Address
from django.urls import reverse_lazy, reverse


class TestView:
    @classmethod
    def setup(cls):
        cls.address = Address.objects.create(
            number=1,
            street='street',
            city='city',
            state='US',
            zip_code=124,
            country_iso_code='ABS'
        )
        cls.letting = Letting.objects.create(
            title='title',
            address=cls.address
        )

        cls.client_test = test.Client()

    @pytest.mark.django_db
    def test_index(self):
        url = reverse('lettings:index')
        response = self.client_test.get(url)
        assert response.status_code == 200
        assert '<title>Lettings</title>' in response.content.decode()
