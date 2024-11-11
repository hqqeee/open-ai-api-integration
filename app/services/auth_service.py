from abs import ABC, abstractmethod


class AuthService(ABC):

    @abstractmethod
    def register(self, username: str, password: str):
        pass

    @abstractmethod
    def login(self, username: str, password: str):
        pass
