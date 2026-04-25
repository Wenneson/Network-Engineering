import requests
from rich import print


BASE_URL = "https://dummyjson.com"

headers = {"Content-Type": "application/json"}

payload = {
    "body": "Hey there just testing this!",
    "userId": 5
}

def main():
    response = requests.post(f"{BASE_URL}/posts/add", headers=headers, json=payload)
    print(response.status_code)
    print(response.text)

if __name__=="__main__":
    main()