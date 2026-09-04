from auth import register, login
from operations import (show_balance, link_card, deposit, withDraw, transfer,
show_transactions,change_password)

users = {}
def main_menu(user, users):
    while True:
        print("\n===== Main Menu =====")
        print("1. View Balance")
        print("2. Link Card")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Transaction History")
        print("7. Change Password")
        print("8. Logout")

        choice = input("Choose: ")

        if choice == "1":
            show_balance(user)
        elif choice == "2":
            link_card(user)
        elif choice == "3":
            deposit(user)
        elif choice == "4":
            withDraw(user)
        elif choice == "5":
            transfer(user, users)
        elif choice == "6":
            show_transactions(user)
        elif choice == "7":
            change_password(user)
        elif choice == "8":
            print("Logged out.\n")
            return
        else:
            print("Invalid choice --> Please pick an option from 1-8.")

def start():
    while True:
        print("\n===== InstaPay =====")
        print("Welcome",__name__)
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ").strip()
        if choice == "1":
            register(users)
        elif choice == "2":
            user = login(users)
            if user is not None:
                main_menu(user, users)
        elif choice == "3":
            print("Thank you for using InstaPay. Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1, 2, or 3.")
if __name__ == "__main__":
    start()
