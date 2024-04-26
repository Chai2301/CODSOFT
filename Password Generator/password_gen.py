import random, string

class PasswordGenerator:
    def __init__(self):
        # Below statements for assigning digits and special characters.
        self.lcase = list(string.ascii_lowercase)
        self.ucase = list(string.ascii_uppercase)
        self.digits = list(string.digits)
        self.punctuations = list(string.punctuation)
        self.user()

    def user(self):
        while True:
            user_input = input("Please enter the length of the password you need: ")
            if not user_input.isdigit():
                print("Please enter a valid number!")
            elif int(user_input) < 6:
                print("Please enter a valid length --> Minimum 6 characters")
            else:
                password = self.generate_password(int(user_input))
                print("-"*50)
                print("Your generated password is:", password)
                print("-"*50)
                break

    def generate_password(self, length):
        characters = self.lcase + self.ucase + self.digits + self.punctuations
        password = ''.join(random.sample(characters, length))
        return password

obj = PasswordGenerator()
