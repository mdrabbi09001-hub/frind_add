import requests

BASE_URL = "https://danger-add-friend.vercel.app"

uid = input("Enter Guest UID: ")
password = input("Enter Guest Password: ")
friend_uid = input("Enter Target UID: ")

url = f"{BASE_URL}/remove_friend"
params = {
    "uid": uid,
    "password": password,
    "friend_uid": friend_uid
}

r = requests.get(url, params=params)
print("\nResponse:\n", r.text)