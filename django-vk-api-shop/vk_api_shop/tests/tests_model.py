from django.test import TestCase

from vk_api_shop.models import ParamsModel


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

    def test_token_label(self):
        params = ParamsModel.objects.get(id=1)
        field_label = params._meta.get_field('token').verbose_name
        self.assertEquals(field_label, 'Token')

    def test_token_max_length(self):
        params = ParamsModel.objects.get(id=1)
        max_length = params._meta.get_field('token').max_length
        self.assertEquals(max_length, 100)

    def test_owner_id_label(self):
        params = ParamsModel.objects.get(id=1)
        field_label = params._meta.get_field('owner_id').verbose_name
        self.assertEquals(field_label, 'Owner_id')

    def test_group_id_label(self):
        params = ParamsModel.objects.get(id=1)
        field_label = params._meta.get_field('group_id').verbose_name
        self.assertEquals(field_label, 'Group_id')

    def test_category_id_label(self):
        params = ParamsModel.objects.get(id=1)
        field_label = params._meta.get_field('category_id').verbose_name
        self.assertEquals(field_label, 'Category_id')

    def test_version_label(self):
        params = ParamsModel.objects.get(id=1)
        field_label = params._meta.get_field('version').verbose_name
        self.assertEquals(field_label, 'Version')

    def test_object_name(self):
        params = ParamsModel.objects.get(id=1)
        expected_object_name = str(params.owner_id)
        self.assertEquals(expected_object_name, str(params))
