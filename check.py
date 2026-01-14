import requests
import json

BASE_URL = "https://danger-add-friend.vercel.app"

uid = input("Enter Guest UID: ")
password = input("Enter Guest Password: ")

url = f"{BASE_URL}/get_friends_list"
params = {
    "uid": uid,
    "password": password
}

r = requests.get(url, params=params)

try:
    data = r.json()

    if isinstance(data, list):
        total = len(data)
        print(f"\nTotal Friends: {total}\n")

        last_100 = data[-100:]
        for i, friend in enumerate(last_100, 1):
            print(f"{i}. {friend}")

    else:
        print("Unexpected response:\n", data)

except:
    print("\nResponse (Raw):\n", r.text)