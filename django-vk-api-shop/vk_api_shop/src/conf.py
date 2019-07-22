from vk_api_shop.models import ParamsModel

try:
    model = ParamsModel.objects.filter(pk=1).first()
    ACCESS_TOKEN = model.token
    GROUP_ID = model.group_id
    OWNER_ID = model.owner_id
    VERSION = model.version
except Exception:
    ACCESS_TOKEN = None
    GROUP_ID = None
    OWNER_ID = None
    VERSION = None

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
