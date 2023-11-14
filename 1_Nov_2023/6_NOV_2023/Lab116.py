class Myclass:

    def __init__(self):
        self.__private_toilet = "Private Toilet Only Pramod Allowed"
        self._protected_attribute = 42
        self.public_var = 55

    def __private_method(self):
        return "This is a private method."
    def _protected_method(self):
        return "This is a private method."



obj = Myclass()
print(obj._protected_attribute)

# Learn about the Private, Protected and Public variables
