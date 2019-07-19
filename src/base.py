import requests


class BaseParser:
    def send_request(self, url: str, params: dict):
        response = requests.get(url, params=params)
        return response.json()

    def upload_file(self, url: str, path_to_file: str):
        files = {
            'file': open(path_to_file, 'rb')
        }
        response = requests.post(url, files=files)
        return response.json()
