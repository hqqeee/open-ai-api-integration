from abs import ABC, abstractmethod

class User:
    def __init__(self, user_id: str, username: str):
        self.user_id = user_id
        self.username = username

    @abstractmethod
    def get_user_id(self):
        pass

    @abstractmethod
    def get_username(self):
        return self.username

    @abstractmethod
    def check_password(self, password: str) -> bool:
        """Checks if the given password matches the stored one."""
        pass
