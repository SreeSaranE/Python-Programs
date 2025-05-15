def check_pass(password: str):
    with open('password.txt', 'r',encoding="utf-8-sig") as file:
        pass_list: list[str] = file.read().splitlines()
        #print(pass_list)
        if (password in pass_list):
            print("Common pass"+':', pass_list.index(password))
        elif (password not in pass_list):
            print("Not a common Password")
        else:
            print("Enter a valid input")

def main():
    user_pass: str = input("Enter your password: ")
    while user_pass == '':
        user_pass: str = input("Enter your password: ")
    check_pass(user_pass)

if __name__ == '__main__':
    main()
