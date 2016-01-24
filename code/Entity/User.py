class User:
    def __init__(self):
        self.userName = ""
        self.password = ""
        self.email = ""

    def get_user_name(self):
        return self.userName

    def set_user_name(self, userName):
        self.userName = userName

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
pass