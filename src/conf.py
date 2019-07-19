ACCESS_TOKEN: str = '116163b7c889f01a3cc1b83cda279cfde3d5d6ee7bb3f6f70250d4986555113be950e1125a0838d8274ab'
GROUP_ID: int = 184546152
OWNER_ID: int = -184546152
VERSION: float = 5.101

get_products_url: str = 'https://api.vk.com/method/market.get'
get_products_params: dict = {
    'access_token': ACCESS_TOKEN,
    'owner_id': OWNER_ID,  # Идентификатор группы
    'album_id': 0,  # Идентификатор альбома
    'count': 100,  # Количество выводимых товаров
    'v': VERSION  # Версия API
}

get_upload_product_image_link_url: str = 'https://api.vk.com/method/photos.getMarketUploadServer'
get_upload_product_image_link_params: dict = {
    'access_token': ACCESS_TOKEN,
    'group_id': GROUP_ID,  # Идентификатор группы
    'main_photo': 1,  # является ли фотография обложкой товара (1 — фотография для обложки, 0 — дополнительная фотография)
    'v': VERSION  # Версия API
}

get_upload_product_image_save_url: str = 'https://api.vk.com/method/photos.saveMarketPhoto'
get_upload_product_image_save_params: dict = {
    'access_token': ACCESS_TOKEN,
    'group_id': GROUP_ID,
    'v': VERSION
}

add_product_url: str = 'https://api.vk.com/method/market.add'
add_product_params: dict = {
    'access_token': ACCESS_TOKEN,
    'owner_id': OWNER_ID,
    'v': VERSION
}
