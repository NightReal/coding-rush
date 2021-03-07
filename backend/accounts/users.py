import bcrypt
from dataclasses import dataclass
import uuid


@dataclass
class User:
    id: int = -1
    email: str = ''
    username: str = ''
    hashed_password: str = ''
    is_activated: bool = False
    activation_token: str = ''

    def __str__(self):
        return f"{self.id} {self.email} {self.username} {self.hashed_password} {self.is_activated} {self.activation_token}"


class Users:
    def __init__(self, database):
        self.db = database

    async def init(self):
        pass

    async def register(self, username: str = '', password: str = '', email: str = ''):
        # TODO: email verification
        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        activation_token = uuid.uuid4()
        id = await self.db.create_user(email, username, password_hash.decode("utf-8"), activation_token.hex)
        print(id)
        user = User(id, email, username, password_hash.decode("utf-8"), False, activation_token.hex)
        print(user)
