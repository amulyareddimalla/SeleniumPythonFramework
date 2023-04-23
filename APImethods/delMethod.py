
import requests
import json

from testcases.api import api_URL
from utilities.readProperties import ReadConfig


class DeleteMethod:
    def delete_data(self):
        # readconfig = ReadConfig()  # create object without any argument
        # self.api_URL = readconfig.getAPIURL()
        try:
            response = requests.delete(api_URL)
            response.raise_for_status()
            print("Request successful with status code: ", + response.status_code)
            print(response)
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
        except json.JSONDecodeError as e:
            print("Error decoding JSON response:", e)