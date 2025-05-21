import time
import string
import itertools

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

def main_program(password: str, pass_length: int):
    char: str = string.ascii_lowercase
    if cap_check(password):
        char = char+string.ascii_uppercase
    if punch_check(password):
        char = char+string.punctuation
    if digits_check(password):
        char = char+string.digits
    
    attempt: int = 0
    for guess in itertools.product(char, repeat=pass_length):
        attempt+= 1
        guess = ''.join(guess)

        if guess == password:
            return(f"{password} was cracked in {attempt}")
        
        #print(guess, attempt)

if __name__ == '__main__':
    user_password: str = input("Enter your password: ")
    start_time = time.perf_counter()
    pass_len: int = len(user_password)
    print(main_program(user_password,pass_len))
    end_time = time.perf_counter()
    total_time = "{:.3f}".format(end_time - start_time)
    print(total_time)
