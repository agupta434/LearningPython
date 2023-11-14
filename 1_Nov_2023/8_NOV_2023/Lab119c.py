class Password:

    def __init__(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
        else:
            print("Weak Password")

    def print_len(self):
        print("Your Password Len is ", len(self.__password))



pwd = Password("Hacker123")
pwd.print_len()
passd = pwd.get_password()
print(pwd.get_password()) # Hacker123
print(passd) # Hacker123

# pwd.set_password("promod")
pwd.set_password("promod123123123")
pwd.print_len() #9 Hacker123