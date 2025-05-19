import string

#alpha = string.ascii_letters+string.digits+string.punctuation

def cap_check(user_password:str):
    for i in user_password:
        if i.isupper:
            return True
        
def punch_check(user_password:str):
    for i in user_password:
        if i in string.punctuation:
            return True

def digits_check(user_password:str):
    for i in user_password:
        if i in string.digits:
            return True

'''
alpha_all = string.ascii_letters+string.digits+string.punctuation
alpha = [char for char in alpha_all]
'''

alpha = string.ascii_lowercase
password: str = ''
repeat: int = 0

#user_password = "saran"
user_password = input("Enter password: ")
if cap_check(user_password):
    alpha = alpha + string.ascii_uppercase
if punch_check(user_password):
    alpha = alpha + string.punctuation
if digits_check(user_password):
    alpha = alpha + string.digits
#alpha = alpha+digits_check(user_password)
user_password_len = len(user_password)
#user_password_text = [char for char in user_password]

while password != user_password:
    print("-----------------")
    for i in user_password:
        for j in alpha:
            print(i,j, "not found")
            if j=='a':
                repeat+=1
            if i==j:
                password = password+j
                print(i, "found")
                print(password,'\n')
                print(repeat)

print(password)
print(repeat)
