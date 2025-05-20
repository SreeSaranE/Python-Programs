import time
import string

def cap_check(user_password:str):
    for i in user_password:
        if i.isupper():
            return True
        
def punch_check(user_password:str):
    for i in user_password:
        if i in string.punctuation:
            return True

def digits_check(user_password:str):
    for i in user_password:
        if i in string.digits:
            return True

alpha = string.ascii_lowercase
password: str = ''
repeat: int = 0

user_password = input("Enter password: ")

start_time = time.time()

if cap_check(user_password):
    alpha = alpha + string.ascii_uppercase
if punch_check(user_password):
    alpha = alpha + string.punctuation
if digits_check(user_password):
    alpha = alpha + string.digits

user_password_len = len(user_password)

while password != user_password:
    for i in user_password:
        for j in alpha:
            if j=='a':
                repeat+=1
            if i==j:
                password = password+j
                #print(password)

end_time = time.time()
total_time = "{:.3f}".format(end_time - start_time)
print(f"Found your password({password}) in {repeat} iterations within {total_time}sec")
