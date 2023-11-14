class Password:

    def __init__(self, password):
        self.__password = password
        # self.public_var = 10
        # self.password = password


    def print_len(self):
        print("Your Password Len is ", len(self.__password))
        # print("Your Password Len is ", len(self.password))


pwd = Password("Hacker123")
pwd.print_len()

# pwd.__password = "abc12456"
print(pwd.__password)
# print(pwd.password)
