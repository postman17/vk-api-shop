from vk_api_shop.src.parsers import Parser

from .models import ParamsModel


class PostIn(Parser):
    @staticmethod
    def vk(instance_model):
        params = ParamsModel.objects.get(pk=1)
        response = Parser.add_product(
            str(instance_model.image.path),
            instance_model.name,
            instance_model.description,
            params.category_id,
            instance_model.price
        )
        return response
