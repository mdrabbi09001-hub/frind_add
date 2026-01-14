import requests
import json
import sys

BASE_URL = "https://danger-add-friend.vercel.app"

uid = input("Enter Guest UID: ")
password = input("Enter Guest Password: ")
friend_uid = input("Enter Target UID: ")

# ===== CHECK FRIEND LIST FIRST =====
check_url = f"{BASE_URL}/get_friends_list"
check_params = {
    "uid": uid,
    "password": password
}

check_req = requests.get(check_url, params=check_params)

try:
    friends = check_req.json()

    if isinstance(friends, list):
        total = len(friends)
        print(f"\nCurrent Friend Count: {total}")

        if total >= 100:
            print("❌ Friend list FULL (100/100)")
            print("❌ Cannot add new friend")
            sys.exit()

    else:
        print("⚠️ Friend list format unknown, trying add...")

except:
    print("⚠️ Could not parse friend list, trying add...")

# ===== ADD FRIEND =====
add_url = f"{BASE_URL}/adding_friend"
add_params = {
    "uid": uid,
    "password": password,
    "friend_uid": friend_uid
}

add_req = requests.get(add_url, params=add_params)
print("\nADD RESPONSE:\n", add_req.text)