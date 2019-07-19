from .base import BaseParser

from src.conf import (
    get_upload_product_image_link_url, get_upload_product_image_link_params,
    get_upload_product_image_save_url, get_upload_product_image_save_params,
    add_product_url, add_product_params
)


class Parser(BaseParser):
    def _get_upload_image_link(self, url: str, params: dict):
        response = Parser().send_request(url, params)
        link = response['response']['upload_url']
        return link

    def _upload_image(self, path_to_image: str):
        link = self._get_upload_image_link(
            get_upload_product_image_link_url,
            get_upload_product_image_link_params
        )
        response = self.upload_file(link, path_to_image)
        return response

    def _save_image(self, url: str, params: dict):
        response = Parser().send_request(url, params)
        return response

    def upload_product_image(self, path_to_image: str):
        upload_file = self._upload_image(path_to_image)
        params = get_upload_product_image_save_params
        params['photo'] = upload_file['photo']
        params['server'] = upload_file['server']
        params['hash'] = upload_file['hash']
        params['crop_data'] = upload_file['crop_data']
        params['crop_hash'] = upload_file['crop_hash']
        response = self._save_image(
            get_upload_product_image_save_url, params
        )
        return response

    @staticmethod
    def get_products(url: str, params: dict):
        products = Parser().send_request(url, params)
        return products

    @staticmethod
    def add_product(path_to_image: str, name: str, description: str, category_id: int, price: float):
        image = Parser().upload_product_image(path_to_image)
        params = add_product_params
        params['main_photo_id'] = image['response'][0]['id']
        params['name'] = name
        params['description'] = description
        params['category_id'] = category_id
        params['price'] = price
        product = Parser().send_request(add_product_url, params)
        return product

