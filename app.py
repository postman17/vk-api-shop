from src.parsers import Parser

from src.conf import (
    get_products_url, get_products_params, get_upload_product_image_link_url,
    get_upload_product_image_link_params
)


# print(Parser.get_products(get_products_url, get_products_params))

# print(Parser().get_upload_image_link(get_upload_product_image_link_url, get_upload_product_image_link_params))

print(
    Parser.add_product(
        '/home/konstantin/github/vk-api-shop/images/unnamed.jpg',
        'Разработка сайтов на python',
        'Разработаем сайт любой сложности', 1, 10000.0
    )
)



