import requests


class ApiHandler:
    def __init__(self, url):
        self.base_url = url

    def get_data(self):
        try:
            result = requests.get(self.base_url)
            status_code = result.status_code

            if status_code == requests.codes.ok:
                return result
            else:
                result.raise_for_status()
        except Exception as ex:
            print(f'Error during data downloading: {ex}')
