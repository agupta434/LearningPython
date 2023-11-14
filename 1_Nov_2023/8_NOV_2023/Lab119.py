class Password:

    def __init__(self, password):
        self.__password = password
        self.public_var = 10

    def get_password(self, is_auth):
        if is_auth:
            return self.__password
        else:
            print("Error")

    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
        else:
            print("Weak Password")

    def print_len(self):
        print("Your Password Len is ", len(self.__password))


pwd = Password("Hacker123")

print(pwd.public_var)

pwd.print_len()
print("--------------------------")
pssd = pwd.get_password()
print(pssd)
pssd1 = pwd.get_password(False)
print(pssd1)

# pwd.__password

pwd.set_password("Pramod123")
pwd.print_len()
