import requests


class ApiHandler:
    @staticmethod
    def get_data(url):
        """
        As a result function returns data from API
        :return: requests' object
        """
        try:
            result = requests.get(url)
            status_code = result.status_code

            if status_code == requests.codes.ok:
                return result
            else:
                result.raise_for_status()
        except Exception as ex:
            print(f'Error during data downloading: {ex}')
