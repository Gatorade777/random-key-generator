import json #for storage the logs in a file 

fill_name = "login.json"

#create a class named login 
class login():
    def __init__(self,name,username_or_email,password,description):
        self.name = name
        self.username_or_email = username_or_email
        self.password = password
        self.description = description

    #show the information about log

    def show_info(self):
        print(f" Name: {self.name}\n Username or email: {self.username_or_email}\n Password: {self.password}\n Description: {self.description}")
    
    #create a profile(object) 

    @staticmethod  #to recall the method 
    def create_profile():
        name = input("What is the name for this login? : ")
        username_or_email = input("Put your name or email for this login sesion: ")
        password = input("Put your secret password here (maybe put the password created in the password generator):  ")
        description = input("description for this login: ")

        return login(name,username_or_email,password,description)

    #convert logins(objects) to dictonarys to store in the file

    def convert_dict(self):
        return {
            "name":self.name,
            "username_or_email":self.username_or_email,
            "password":self.password,
            "description":self.description
        }

#store dictonarys in the file (for the moment store only one profile :c)

def save_profile(profile, fill_name="login.json"):
    with open(fill_name, "w") as file: #write in the file 
        json.dump(profile.convert_dict(), file, indent=4)



#create a object to store this login
new_login = login.create_profile()
new_login.show_info()
save_profile(new_login)