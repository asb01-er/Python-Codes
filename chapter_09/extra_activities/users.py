class User:
    def __init__(self,first_name,last_name,location):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location 
        self.login_attempts = 0
    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name}"
        print(f"User Name: {full_name.title()}")
        print(f"User Location: {self.location}")

    def increment_login_attempts(self,logins):
        if logins >= self.login_attempts:
            self.login_attempts + 1
            print(f"You attempted {logins} times!")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"You attempted {self.login_attempts} times!")

    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Welcome Back {full_name.title()}!")

user_1 = User('ernest','ekelem','joburg')
user_2 = User('michael','groening','cape town')

user_1.describe_user()
user_1.greet_user()

# user_2.describe_user()
# user_2.greet_user()

user_1.increment_login_attempts(5)
user_1.reset_login_attempts()


