#well iam newbi so this is mi first proyect, if a make some mistakes i accept correptions also i dont speak inglish


#code idea---->

#def the function to generate the random password
import random as rm #for random characters
import string as st #for all the characters in the paswword

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

    password = "".join(rm.choice(characters) for _ in range(length)) #add the charcacters that you choose in a random place with the length you choose(i dont know if that is a corret grammar)
    return password

#ask the length of the password, ask if want lower and upper cases, also ask if want special charactes,
def main():#maybe this function has to be ahead of the other XD
    attempts = 0
    attempts2 = 0
    #bucle for attemps in the length
    while True:
        
        try:
            
            length = int(input("enter(in number) the length of the password that you want: "))
            if length <= 0:
                if attempts2 == 2:
                    print("you're really stupid bro xd")
                    break
                attempts2 += 1
                print("only positive numbers ")
            else:
                break
        except ValueError:#because the other valueError
            
            if attempts == 2:
                print("you're really stupid bro xd")
                break
            attempts  += 1
            print("pls enter a valid NUMBER for the length of your password")#this is in case the user dont put a number in the lenght
    
        
                
    if attempts == 2 or attempts2 == 2:
        return print("sorry we cant create your password, try again")
    else:
        numbers = input("you want use numbers in the password? (y/n)").lower() == "y"
        upper = input("you want use upper cases in the password? (y/n)").lower() == "y" #in this case if the user respond y o Y upper become True if respond somenthing else is false
        special = input("you want to use special characters for you password? (y/n)").lower() == "y"
    
        password = random_key_generator(length, numbers, upper, special)
        print(f"Here is your ultra professional secret password: {password}")
    
        
            
main()
    






