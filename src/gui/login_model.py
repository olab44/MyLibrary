from database import Database


class LoginModel:
    def __init__(self):
        self.database = Database()
        query = "select * from users;"
        self.users_info = self.database.fetch_data(query)

    def find_user(self, user_name):
        for user_info in self.users_info:
            id, username, password = user_info
            if username == user_name:
                return user_info
        return None

    def check_user_password(self, user):
        if not self.find_user(user):
            return None
        _, _, password = self.find_user(user)
        return password

    def if_valid(self, username, password):
        user_info = self.find_user(username)
        if user_info:
            _, _, stored_password = user_info
            if password == stored_password:
                return True
        return False

    def login(self, username, password):
        return self.if_valid(username, password)
