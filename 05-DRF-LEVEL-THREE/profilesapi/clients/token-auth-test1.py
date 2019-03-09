import requests

def client():
    # credentials = {"username": "admin", "password": "asdasdasd"}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                          data=credentials)

    token_h = "Token affe5406283b7471e28f596cd5a13a19c05080b3"
    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)

    print("Status Code: ", response.status_code)
    
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()