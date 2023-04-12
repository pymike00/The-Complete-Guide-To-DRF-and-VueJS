import requests


def main():
    response = requests.get("https://www.google.com")
    # response = requests.get("https://www.google.com/random-address/")
    print("Status Code: ", response.status_code)
    # print("Headers: ", response.headers)
    # print("'Content-Type': ", response.headers['Content-Type'])
    print("Content: ", response.text)


if __name__ == "__main__":
    main()
