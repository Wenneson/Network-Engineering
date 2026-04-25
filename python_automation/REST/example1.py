import requests
from rich import print


BASE_URL = "https://dummyjson.com"

def main():
    response = requests.get(f"{BASE_URL}/users")
    print(response.status_code)
    print(response.json()["users"][0]["firstName"])

if __name__=="__main__":
    main()