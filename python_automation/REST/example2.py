import requests
from rich import print


BASE_URL = "https://dummyjson.com"

def main():
    response = requests.get(f"{BASE_URL}/comments")
    print(response.status_code)
    print(response.json())

if __name__=="__main__":
    main()