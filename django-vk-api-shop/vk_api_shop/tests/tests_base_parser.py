from django.test import TestCase

from vk_api_shop.models import ParamsModel
from ..post import PostIn
from ..src.conf import get_products_url


class ParamsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ParamsModel.objects.create(
            token='978194bc371eb2f1fa151be516b760b66b4d7724fd6ea6453259e07df7df6b004c4450fc3598a9882d900',
            owner_id=-184546200,
            group_id=184546200,
            category_id=1201,
            version=5.101
        )

    def test_send_request(self):
        params = ParamsModel.objects.get(id=1)
        response = PostIn().send_request(
            url=get_products_url,
            params={
                'access_token': params.token,
                'owner_id': params.owner_id,
                'album_id': 0,
                'count': 100,
                'v': params.version
            }
        )
        self.assertEquals(
            response, {'error':
                           {
                               'error_code': 5,
                                'error_msg': 'User authorization failed: invalid access_token (4).',
                               'request_params':
                                   [
                                       {'key': 'owner_id', 'value': '-184546200'},
                                       {'key': 'album_id', 'value': '0'},
                                       {'key': 'count', 'value': '100'},
                                       {'key': 'v', 'value': '5.101'},
                                       {'key': 'method', 'value': 'market.get'},
                                       {'key': 'oauth', 'value': '1'}
                                   ]
                           }
            }
        )
