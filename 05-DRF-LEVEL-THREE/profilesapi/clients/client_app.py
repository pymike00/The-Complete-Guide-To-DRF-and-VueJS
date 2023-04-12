import requests


def registration(account_data: dict) -> None:
    registration_endpoint = "http://127.0.0.1:8000/api/dj-rest-auth/registration/"
    response = requests.post(registration_endpoint, data=account_data)
    print(response)


def login(login_credentials: dict) -> str:
    login_endpoint = "http://127.0.0.1:8000/api/dj-rest-auth/login/"
    response = requests.post(login_endpoint, data=login_credentials)
    status_code = response.status_code
    print(f"Status Code: {response.status_code}")
    if status_code == 200:
        auth_token = response.json()["key"]
        print(f"Auth Token: {auth_token}")
        return auth_token


def client(auth_token: str, endpoint: str) -> None:
    token_h = f"Token {auth_token}"
    headers = {"Authorization": token_h}
    response = requests.get(endpoint, headers=headers)
    status_code = response.status_code
    print(f"Status Code: {response.status_code}")
    if status_code == 200:
        response_data = response.json()
        print(response_data)


if __name__ == "__main__":
    # account_data = {
    #     "username": "mytestuser",
    #     "email": "test@myrest.com",
    #     "password1": "verystrongpassword",
    #     "password2": "verystrongpassword",
    # }
    # registration(account_data)

    login_credentials = {"username": "mytestuser", "password": "verystrongpassword"}
    auth_token = login(login_credentials)

    data_endpoint = "http://127.0.0.1:8000/api/profiles/"
    client(auth_token, data_endpoint)
