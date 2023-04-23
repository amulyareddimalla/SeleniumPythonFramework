import requests
from utilities.readProperties import ReadConfig


class Get_User:
    def __init__(self):
        self.base_url = ' '

    def get_user_validation(self):
        readconfig = ReadConfig()  # create object without any argument
        self.user_id_api = readconfig.getUserID()

        try:
            url = f'{self.base_url}/users?email={self.user_id_api}'
            response = requests.get(url)
            if response.ok:
                return response.json()[0]
            else:
                raise Exception(f'Failed to get user data. Status code: {response.status_code}')
        except Exception as e:
            raise Exception(f'Error occurred while getting user data: {e}')

