"""
Note: we are using a free API that provides data on the exchange rates of different currencies.
Access to this API might be limited in the future, and providing a valid API key might be required to access the API.
We are in no way affiliated with the API provider, and we are not responsible for any changes to the API.

Keeping the code up to date with a working hardcoded API endpoint goes beyond the scope of this code and the course itself.
You can find a list of public APIs here: https://github.com/public-apis/public-apis
"""

import requests


def main():
    response = requests.get("https://api.frankfurter.app/latest")

    if response.status_code != 200:
        print("Status Code: ", response.status_code)
        raise Exception("There was an error!")

    data = response.json()
    print("JSON data: ", data)


if __name__ == "__main__":
    main()
