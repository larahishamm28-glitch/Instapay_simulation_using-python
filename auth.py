from validation import ( validate_username, validate_password, validate_phone )

##maximum number of login attempts before locking the account
MAX_LOGIN_ATTEMPTS = 3

def find_user(username, users):
    ##search for a user by username in the users dict
    #Lara: el user met5azena fi el register() as dictionary fa henaa
    #el find_user btrag3 direct men el dict - msh loop zay list
    return users.get(username)

def register(users):
    ##register a new user by collecting username, password, and phone number

    print("=======Register=======")

    name = input("Enter your name: ").strip()

    ##make sure the name is not empty
    while len(name) == 0:
        print("Name cannot be empty")
        name = input("Enter your name: ").strip()


    ###validate the phone number
    while True:
        phone = input("Enter your phone number: ").strip()

        is_valid, message = validate_phone(phone)

        if is_valid:
            break

        print(message)

    ###validate the username
    while True:
        username = input("Enter your username: ").strip()

        is_valid, message = validate_username(username, users)

        if is_valid:
            break

        print(message)

    ##validate the password
    while True:
        password = input("Enter your password: ").strip()

        is_valid, message = validate_password(password)

        if is_valid:
            break

        print(message)

    ## create the username acount
    users[username] = {
        'username': username,
        'name': name,
        'phone': phone,
        'password': password,
        'balance': 0.0,
        "card": None,
        "transactions": []
    }

    ### show successful registration message
    print (f"User {username} registered successfully!")

    return users[username]


def login(users):
    ##login a user by collecting username and password

    print("=======Login=======")

    attempts_left = MAX_LOGIN_ATTEMPTS

    ##keep asking until the user logs in or runs out of attempts
    while attempts_left > 0:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        user = find_user(username, users)

        if user is not None and user['password'] == password:
            print(f"Welcome back, {user['name']}!")
            return user

        print("invalid username or password, Please try again")
        attempts_left -= 1

        ###show remaining attempts if there are any
        if attempts_left > 0:
            print(f"Attempts remaining: {attempts_left}")

    print("too many failed attempts")
    print("Returning to main menu")

    return None