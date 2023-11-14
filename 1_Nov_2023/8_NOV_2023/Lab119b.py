class Password:

    def __init__(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def print_len(self):
        print("Your Password Len is ", len(self.__password))



pwd = Password("Hacker123")
pwd.print_len()
passd = pwd.get_password()
print(pwd.get_password())
print(passd)

# pwd.__password = "abc12456"
# print(pwd.__password)
# print(pwd.password)
