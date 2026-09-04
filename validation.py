# checking : username -password -phone- amount(Deposit / Withdraw / Transfer) 
#            card number -CVV -espiry

def validate_username ( username ,user): 
    ##username must be non-empty,no spaces, unique
    
    username = username.strip()
    
    if len(username) == 0 :
        return False ," Username can not be empty!!"
    
    if " " in username :
        return False, "Username cannot contain spaces !!"
    
    if username in user : 
        return False, "that username is already taken"
    
    return True , ""


def validate_password(password):
    ##password must be at least 6 characters
    
    if len(password) < 6:
        return False , "Pasword must be at least 6 characters"
    
    return True ,""


def validate_phone(phone):
    ## phone must contain exactly 11 digits ,no spaces
    
    phone = phone.strip()
    
    if not phone.isdigit():
        return False ,"phone number must be digits only"
    
    if len(phone) != 11 :
        return False ,"phone number must be 11 digits long"
    
    return True , ""


def validate_amount(amount_str):
    ##amount must be a valid number greater than zero

    try:
        amount = float (amount_str)
    
    except ValueError:
        return False, "invalid , please enter a number",None
    
    if amount <= 0 :
        return False ,"amount must be greater than 0" ,None
    
    return True , "",amount


def validate_card_number(card_number):
    ##card number must be exactly 16 digits
    
    card_number=card_number.strip ()
    
    if len(card_number)!= 16:
        return False,"card number must be 16 digits"
    
    if not card_number.isdigit():
        return False,"card number must contain digits only "
    
    return True ,""


def validate_cvv(cvv):
    ##CVV must be exactly 3 digits
    
    cvv = cvv.strip()
    
    if len(cvv) != 3:
        return False,"CVV must be 3 digits only"
    
    if not cvv.isdigit():
        return False , "CVV must contain digits only"
    
    return True , ""

def validate_expiry(expiry):
    ##Expiry date must follow MM/YY format
    
    expiry = expiry.strip()
    parts = expiry.split("/")
    
    if len(parts) != 2:
        return False ,"expiry data must be in MM/YY format"
    
    month , year = parts
    
    
    if not (month.isdigit() and year.isdigit()):
        return False, "expiry date must be in MM/YY format"

    if len(month) != 2 or len(year) != 2:
        return False, "expiry date must be in MM/YY format"

    if not (1 <= int(month) <= 12):
        return False, "expiry month must be between 01 and 12"

    return True, ""