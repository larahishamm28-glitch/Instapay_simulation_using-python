# Instapay_simulation_using-python
# 💳 InstaPay Simulation

This is our Python mini project - a simple console-based digital wallet app (like a mini version of Instapay/Vodafone Cash) that we built to practice functions, dictionaries, loops, input validation, and splitting code into multiple files.

## What it does

It's a simulation of a digital wallet that runs in the terminal. You can:

- Register a new account
- Login (max 3 attempts, then it kicks you back to the menu)
- Link a Visa card
- Deposit money
- Withdraw money
- Transfer money to another user
- View your transaction history
- Change your password (bonus feature I added)

## Why we split it into files

At first we had everything in one file and it got really messy fast, so we split it based on what each part actually does:

```
InstaPay_Simulation/
│
├── main.py          -> runs the app, shows the menus
├── auth.py           -> register / login stuff
├── validation.py      -> checks if user input is valid
└── operations.py      -> deposit, withdraw, transfer, balance, card, history
```

So basically:
- `main.py` doesn't do any actual logic, it just shows menus and calls functions from the other files
- `auth.py` handles the users dictionary + register/login
- `validation.py` only checks input (like is the phone number 11 digits, is the amount a positive number, etc). It doesn't print anything, it just returns True/False + a message
- `operations.py` has all the money-related functions

## How to run it

```
python main.py
```

Then just follow the menu. Suggested order to try it out:

Register -> Login -> Link Card -> Deposit -> Check Balance -> Transfer -> Withdraw -> Transaction History -> Logout

(you'll need to register at least 2 accounts to actually test the transfer feature)

## Some things we made sure to handle

- Can't transfer money to yourself
- Can't withdraw/transfer more than your balance
- Password and CVV never get printed anywhere
- Every deposit/withdraw/transfer gets logged in a transaction history list

## Team

This was a group project between two of us:

- **Jolie** - worked on `auth.py` and `validation.py`
- **Lara** - worked on `operations.py` and `main.py`
