import string
punch = [char for char in string.punctuation]

def check_pass(password: str):
    with open('password.txt', 'r',encoding="utf-8-sig") as file:
        pass_list: list[str] = file.read().splitlines()
        #print(pass_list)
        if (password in pass_list):
            print("Common pass"+':', pass_list.index(password))
        elif (password not in pass_list):
            pass_len: int = len(password)
            if (pass_len <= 8):
                print(f"🟥The lenght of the password({password}) is too small!")
            else:
                print("🟩The pass has enough characters")
            pass_split = [char for char in password]
            special_check = 0
            case_check = 0
            for i in pass_split:
                if i.isupper():
                    case_check = 1
                for j in punch:
                    if i == j:
                        print(f"🟩Your password({password}) contain special characters")
                        special_check = 1
            if (special_check != 1):
                print(f"🟥Your password({password}) doesn't contain any special characters")
            if (case_check != 1):
                print(f"🟥Your password({password}) doesn't contain any Upper Case")
            else:
                print(f"🟩Your password({password})contain Upper Case")

def main():
    user_pass: str = input("Enter your password: ")
    while user_pass == '':
        user_pass: str = input("Enter your password: ")
    check_pass(user_pass)

if __name__ == '__main__':
    main()
