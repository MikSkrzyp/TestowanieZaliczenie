class UserManager:
    def __init__(self):
        self.database = {
            1: "Alice",
            2: "Oskar"
        }

    def get_user(self, user_id):
        return self.database.get(user_id)

    def get_all_users(self):
        return self.database.copy()

    def add_user(self, user_id, name):
        if user_id in self.database:
            return f"User with id {user_id} already exists."
        self.database[user_id] = name
        return f"User {name} added with id {user_id}."

    def update_user(self, user_id, name):
        if user_id in self.database:
            self.database[user_id] = name
            return f"User id {user_id} updated to {name}."
        return f"User with id {user_id} does not exist."

    def delete_user(self, user_id):
        if user_id in self.database:
            del self.database[user_id]
            return f"User with id {user_id} deleted."
        return f"User with id {user_id} does not exist."
