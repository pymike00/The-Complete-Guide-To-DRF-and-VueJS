import requests

def main():
    # response = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=GBP")

    payload = {"base": "USD", "symbols": "SEK"}
    response = requests.get("https://api.exchangeratesapi.io/latest",
                            params=payload)
    
    if response.status_code != 200:
        print("Status Code: ", response.status_code)
        raise Exception("There was an error!")

    data = response.json()
    print("JSON data: ", data)



if __name__ == "__main__":
    main()