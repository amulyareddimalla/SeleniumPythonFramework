import json
import requests
from utilities.readProperties import ReadConfig

readconfig = ReadConfig()  # create object without any argument
api_URL = readconfig.getAPIURL()

try:
    response = requests.get(api_URL)
    response.raise_for_status() # raise exception if status code is not 200
    data = response.json()
    print("Request successful with status code: ", + response.status_code)
    print(json.dumps(data, indent=2)) #to make the JSON output redeable
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
except json.JSONDecodeError as e:
    print("Error decoding JSON response:", e)
