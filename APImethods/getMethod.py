import json
import requests
from testcases.api import api_URL
class GetMethod:
    def get_data(self):

        try:
            response = requests.get(api_URL)
            response.raise_for_status()
            data = response.json()
            print("Request successful with status code: ", + response.status_code)
            print(json.dumps(data, indent=2))
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
        except json.JSONDecodeError as e:
            print("Error decoding JSON response:", e)



