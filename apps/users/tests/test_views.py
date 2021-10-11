from django.urls import reverse

from rest_framework.test import APIClient


def test_users_view(api_client: APIClient):
    url = reverse('users:users')

    response = api_client.get(url)

    assert response.json() == [
        {
            'id': 1,
            'username': 'My username',
            'profile': {
                'email': 'admin@gmail.com',
                'social_security_number': 'SSN <#12345678>'
            },
            'groups': [
                {'name': 'Users'},
                {'name': 'Admins'}
            ]
        }
    ]
