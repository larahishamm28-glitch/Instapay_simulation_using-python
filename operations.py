from validation import(validate_amount, validate_card_number,
validate_cvv, validate_expiry, validate_password)
from auth import (find_user)

#print users Balance
def show_balance(user):
    print("============Balance============")
    print(user['balance'])

#Deposit
def deposit(user):
    print("\n============ Deposit =============")

    while True:
        raw_amount = input("Enter amount: ")
        is_valid, message, amount = validate_amount(raw_amount)

        if is_valid:
            break          # go out of the loop if valid

        print(message)     # print

    # Add the deposited amount to the user's current balance
    # and save the result back into user['balance']
    user['balance'] = user['balance'] + amount

    # Log this deposit in the user's transaction history
    user['transactions'].append({'type': 'Deposit', 'amount': amount})

    # Show a confirmation message with the updated balance
    print(f"Deposit successful! New Balance: {user['balance']} EGP")


def withDraw (user):
    print("\n============ Withdraw =============")
    # Keep asking for an amount until the user enters a valid one
    while True:
        raw_amount = input("Enter amount: ")
        is_valid, message, amount = validate_amount(raw_amount)

        if is_valid:
            break      # got a valid amount so exit the loop

        print(message)     #  if invalid inputs how why and ask again

    # Check that the user has enough balance Before removing anything
    # If not, stop the function here with return so nothing gets deducted
    if amount > user['balance']:
        print("Insufficient balance. Withdrawal cancelled.")
        return

    # If the balance was enough
    # so subtract the amount from the user's balance
    user['balance'] -= amount

    # Log this withdrawal in the user's transaction history
    # (stored as a negative amount, same style as Transfer)
    user['transactions'].append({'type': 'Withdraw', 'amount': -amount})

    # Show a confirmation message with the updated balance
    print(f"Withdrawal successful! Remaining Balance: {user['balance']} EGP")


#Input: card number, card holder name, expiry date, CVV. Basic validation applies.
def link_card(user):
    print("\n===== Link Visa Card =====")

    # Ask for the card number until it passes validation
    while True:
        card_number = input("Card number (16 digits): ")
        is_valid, message = validate_card_number(card_number)
        if is_valid:
            break #exit looop
        print(message)

    # Holder name just make sure it's not empty
    holder_name = input("Card holder name: ").strip()
    while len(holder_name) == 0:
        print("Card holder name cannot be empty.")
        holder_name = input("Card holder name: ").strip()

    # Ask for expiry date
    while True:
        expiry = input("Expiry date (MM/YY): ")
        is_valid, message = validate_expiry(expiry)
        if is_valid:
            break
        print(message)

    # Ask for CVV to pass validation
    while True:
        cvv = input("CVV (3 digits): ")
        is_valid, message = validate_cvv(cvv)
        if is_valid:
            break
        print(message)

    # Save the card info - notice CVV is NOT stored here.
    # It was only used to validate the format, then thrown away.
    user['card'] = {
        'number': card_number,
        'holder_name': holder_name,
        'expiry': expiry
    }
    print("Card linked successfully!")


#Transfer Moneey
def transfer(user, users):
    print("\n===== Transfer =====")
    recipient_username = input("Recipient username: ").strip()

    # condition 1: can't send money to yourself(same user)
    if recipient_username == user['username']:
        print("You cannot transfer money to yourself.")
        return

    # condition 2: recipient must actually exist
    recipient = find_user(recipient_username, users)
    if recipient is None:
        print("Recipient not found. Transfer cancelled.")
        return

    # Ask for the amount
    while True:
        raw_amount = input("Amount: ")
        is_valid, message, amount = validate_amount(raw_amount)
        if is_valid:
            break
        print(message)

    # condition 3: sender must have enough balance(check balance)
    if amount > user['balance']:
        print("Insufficient balance. Transfer cancelled.")
        return

    # condition 4: ask for a final confirmation
    confirm = input(f"Confirm transfer of {amount} EGP to {recipient_username}? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Transfer cancelled.")
        return

    # Move the money subtract from sender and add to recipient
    user['balance'] -= amount
    recipient['balance'] += amount

    # Log the transaction on both sides
    user['transactions'].append({'type': 'Transfer', 'amount': -amount, 'to': recipient_username})
    recipient['transactions'].append({'type': 'Transfer', 'amount': amount, 'to': user['username']})

    print(f"Transfer successful! Your new balance: {user['balance']} EGP")


#Show Transactions
def show_transactions(user):
    print("\n============ Transaction History ============")

    # If the list is empty print a message and stop
    if not user['transactions']:
        print("No transactions yet.")
        return

    # enumerate() to give the item and it positin
    for index, tx in enumerate(user['transactions'], start=1):
        sign = "+" if tx['amount'] >= 0 else ""
        line = f"{index}. {tx['type']} {sign}{tx['amount']} EGP"

        # Transfers have a to key
        if 'to' in tx:
            line += f" (to/from {tx['to']})"

        print(line)


#Chamge password (Bonus)
def change_password(user):
    print("\n===== Change Password =====")

    # First confirm they actually know the current password
    current = input("Current password: ")
    if current != user['password']:
        print("Incorrect current password.")
        return

    # Then validate and set the new one
    while True:
        new_password = input("New password (min 6 characters): ")
        is_valid, message = validate_password(new_password)
        if is_valid:
            break
        print(message)

    user['password'] = new_password
    print("Password changed successfully!")