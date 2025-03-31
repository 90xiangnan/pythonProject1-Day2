import json


class UserManager:
    def __init__(self, file_path="users.json"):
        self.file_path = file_path
        try:
            with open(self.file_path, 'r') as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = {}

    def save_user_info(self, username, password, score=0):
        self.users[username] = {
            "username": username,
            "password": password,
            "score": score
        }
        with open(self.file_path, 'w') as f:
            json.dump(self.users, f, indent=4)

    def verify_user(self, username, password):
        user = self.users.get(username)
        password1 = user["password"]
        if user and user["password"] == password:
            return True
        return False

    def get_user_score(self,username):
        return self.users.get(username, {}).get("score", 0)

    def update_user_score(self,username, score):
        mypassword = self.users.get(username, {}).get("password", 0)
        self.users[username] = {
            "username": username,
            "password": mypassword,
            "score": score
        }
        with open(self.file_path, 'w') as f:
            json.dump(self.users, f, indent=4)


