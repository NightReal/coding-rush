from passlib.hash import bcrypt_sha256
import uuid
import models


async def register(db, username: str = '', password: str = '', email: str = ''):
    # TODO: email verification
    password_hash = bcrypt_sha256.hash(password)
    activation_token = uuid.uuid4()
    new_user = models.User(email=email, username=username, hashed_password=password_hash, is_activated=False, activation_token=activation_token.hex)
    return new_user
