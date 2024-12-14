import random
import string

def password_creater(length):
    
    if(length<4):
        print("Too short length ")
        return

    num = string.digits
    up_letters = string.ascii_uppercase
    lo_letters = string.ascii_lowercase
    sp_character = string.punctuation

    password = [
        random.choice(num),
        random.choice(up_letters),
        random.choice(lo_letters),
        random.choice(sp_character)
    ]

    all_character = num+up_letters+lo_letters+sp_character

    password += random.choices(all_character,k= length-4)
    
    password = ''.join(password)

    return password


    
if __name__ == "__main__":
     
    txt = "Welcome to password generator"

    print(txt.center(50,'-'))

    length = int(input("Enter the length of password: "))

    result = password_creater(length)

    if(result == None):
        print("Please increase the length of password")

    else:
        print("Password Generated successfuly!")
        print(f"Your generated password is: {result}")

    

    



