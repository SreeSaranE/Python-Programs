def check_pass(password: str):
    with open('password.txt', 'r',encoding="utf-8-sig") as file:
        pass_list: list[str] = file.read().splitlines()
        #print(pass_list)
        if (password in pass_list):
            print("Common pass")
        elif (password not in pass_list):
            print("Not a common Password")
        else:
            print("Enter a valid input")
    
user_pass: str = input("Enter your password: ")

def main():
    check_pass(user_pass)

if __name__ == '__main__':
    main()