#Password generator by Gatorade777


#code idea----> A program that allows the user to create a secure password that can be stored locally and used when login is required.


import random as rm #for random characters
import string as st #for all the characters in the paswword


def create():
    pass #dont work yet
    #while True:
        #response = input("you want create a new login? (y/n)").lower() == "y"
        #if response:
            #return False
        #else:
            #return 

    



#def the function to generate the random password
def random_key_generator(length,numbers,upper,special):
    characters = st.ascii_lowercase #the password by default has lower cases
    if upper:
        characters += st.ascii_uppercase
    if numbers:
        characters += st.digits
    if special:
        characters += st.punctuation
    if not characters:
        raise ValueError

    password = "".join(rm.choice(characters) for _ in range(length))#Adds the character(s) of your choice at a random location with a length of your choice.
    return password

#Ask for the length of the password, ask if they want lowercase and uppercase letters, and ask if they want special characters


def main():
    attempts = 0
    attempts2 = 0
    if not create:
        return
    #bucle for attemps in the length
    while True:
        
        try:
            
            length = int(input("Enter the desired password length (in numbers). The minimum recommended for a strong password is 8:  "))
            if length <= 0:
                if attempts2 == 2:
                    print("you're really stupid bro xd")
                    break
                attempts2 += 1
                print("Non-zero positive numbers only ")
            else:
                break
        except ValueError:
            
            if attempts == 2:
                print("you're really stupid bro xd")
                break
            attempts  += 1
            print("Enter a valid NUMBER for your password length.")#This is in case the user does not enter a valid number in length.
    
        
                
    if attempts == 2 or attempts2 == 2:
        return print("sorry we cant create your password, try again")
    else:
        #in this case if the user respond y o Y upper become True if respond somenthing else is false
        numbers = input("Do you want to use numbers in the password? (y/n):").lower() == "y"
        upper = input("Do you want to use uppercase letters in the password? (y/n):").lower() == "y" 
        special = input("Do you want to use special characters in your password? (y/n):").lower() == "y"
    
        password = random_key_generator(length, numbers, upper, special)
        print(f"Here is your ultra professional secret password: {password}")
    
        
create()          
main()







