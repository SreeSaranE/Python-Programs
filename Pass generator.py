import string, secrets

def caps_yes(password: str) -> bool:
    for char in password:
        if char.isupper:
            return True
    return False

def symbol_yes(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def make_pass(lenght: int, upper: str, symbol: str) -> str:
    combination = string.digits + string.ascii_lowercase
    if upper == "Y":
        combination += string.ascii_uppercase
    if symbol == "Y":
        combination += string.punctuation

    com_length: int = len(combination)
    Password: str = ''

    for _ in range(lenght):
        Password += combination[secrets.randbelow(com_length)]
    
    return Password

while True:
    try:
        Length = int(input("Enter the Password Length: "))
        if Length <= 2:
            print("The Password length should be a minimum of 3 digits")
        else:
            break
    except ValueError:
        print("Please enter a valid number")

Upper: str = input("Enter whether the Password should contain UpperCase or not (Y/N): ")
while Upper.upper() not in ['Y', 'N']:
    print("Provide a valid Input")
    Upper: str = input("Enter whether the Password should contain UpperCase or not (Y/N): ")

Symbol: str = input("Enter whether the Password should contain Special Symbols or not (Y/N): ")
while Symbol.upper() not in ['Y', 'N']:
    print("Provide a valid Input")
    Symbol: str = input("Enter whether the Password should contain Special Symbols or not (Y/N): ")

New_pass = make_pass(Length, Upper.upper(), Symbol.upper())  
print(f"The generated Password is {New_pass}")
