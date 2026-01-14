import os
import sys
import time

def clear():
    os.system("clear")

def banner():
    print("=" * 45)
    print("   FREE FIRE FRIEND MANAGER")
    print("   Developer : INDRAJIT")
    print("=" * 45)

def menu():
    print("\n[1] Add Friend")
    print("[2] Remove Friend")
    print("[3] Check Friend List (Last 100)")
    print("[0] Exit")

while True:
    clear()
    banner()
    menu()

    choice = input("\nSelect Option : ")

    if choice == "1":
        clear()
        os.system("python add.py")
        input("\nPress Enter to return menu...")

    elif choice == "2":
        clear()
        os.system("python remove.py")
        input("\nPress Enter to return menu...")

    elif choice == "3":
        clear()
        os.system("python check.py")
        input("\nPress Enter to return menu...")

    elif choice == "0":
        print("\nExit Successfully ✔")
        sys.exit()

    else:
        print("\nInvalid Option ❌")
        time.sleep(1)