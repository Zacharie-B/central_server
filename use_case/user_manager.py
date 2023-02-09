from entities.user import User


class UserManager:
    def __init__(self):
        self.__users = []

    def is_registered(self, username):
        for us in self.__users:
            if us.get_username() == username:
                return us.get_password()
        return 0

    def choice_authent_method(self, credentials):
        us = credentials[0]
        pw = credentials[1]
        pwd = self.is_registered(us)
        if pwd:
            res = self.signin(pwd, pw)
        else:
            res = self.register(us, pw)
        return res

    def signin(self, pwd, password):
        if password == pwd:
            return "Authentification réussie"
        return "Authentification échoué"

    def register(self, us, pw):
        user = User(us, pw)
        self.__users.append(user)
        return "Inscription réussie"

    def get_users(self):
        return self.__users
