import asyncio
import models

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, settings):
        self.host = settings.POSTGRES_HOST
        self.db = settings.POSTGRES_DB
        self.user = settings.POSTGRES_USER
        self.password = settings.POSTGRES_PASSWORD

    async def init(self):
        self.engine = create_async_engine(
            f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.db}"
        )
        async with self.engine.begin() as conn:
            await conn.run_sync(models.Base.metadata.drop_all)
            await conn.run_sync(models.Base.metadata.create_all)

        self.async_session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )

    async def create_user(self, user: models.User):
        async with self.async_session() as session:
            session.add(user)
            await session.commit()


async def main():
    engine = create_async_engine(
        "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
    )
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)

    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    async with async_session() as session:
        n = User(email='asdf@as.as', username='user', hashed_password='aaaaa', is_activated=True, activation_token='adasd')
        session.add(n)
        await session.commit()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
