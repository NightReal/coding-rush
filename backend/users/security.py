import sqlalchemy as sa
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from db import User, Database, Permission

from aiohttp_security.abc import AbstractAuthorizationPolicy
from passlib.hash import bcrypt_sha256
import uuid


class DBAuthorizationPolicy(AbstractAuthorizationPolicy):
    def __init__(self, engine: Database):
        self.engine = engine

    async def permits(self, identity, permission, context=None):
        if identity is None:
            return False

        async with self.engine.async_session() as session:
            where = sa.and_(User.username == identity, sa.not_(User.disabled))
            query = select(User).options(selectinload(where))
            ret = await session.execute(query)
            user = await ret.fetchone()
            if user is None:
                return False
            user_id = user.id
            if user.is_superuser:
                return True

            where = Permission.user_id == user_id
            query = select(Permission).options(selectinload(where))
            ret = await session.execute(query)
            res = await ret.fetchall()
            if ret is not None:
                for record in res:
                    if record.perm_name == permission:
                        return True
        return False

    async def authorized_userid(self, identity):
        async with self.engine.async_session() as session:
            where = sa.and_(User.username == identity, sa.not_(User.disabled))
            query = select(User).options(selectinload(where))
            ret = await session.scalar(query)
            if ret:
                return identity
            return None


async def register(database: Database, username: str = '', password: str = '', email: str = ''):
    # TODO: email verification
    password_hash = bcrypt_sha256.hash(password)
    activation_token = uuid.uuid4()
    new_user = User(email=email, username=username, hashed_password=password_hash, is_activated=False, activation_token=activation_token.hex)
    async with database.async_session() as session:
        session.add(new_user)
        await session.commit()
