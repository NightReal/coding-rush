from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

Base = declarative_base()


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
            await conn.run_sync(Base.metadata.reflect)

        self.async_session = sessionmaker(
            self.engine, expire_on_commit=False, class_=AsyncSession
        )


class User(Base):
    __tablename__ = "users"
    __mapper_args__ = {"eager_defaults": True}

    id = Column(Integer, primary_key=True, unique=True)
    email = Column(Text, nullable=False, unique=True)
    username = Column(Text, nullable=False, unique=True)
    hashed_password = Column(Text, nullable=False)
    is_activated = Column(Boolean, nullable=False, default=False)
    activation_token = Column(Text, nullable=False)
    is_superuser = Column(Boolean, default=False)
    disabled = Column(Boolean, default=False)


class Permission(Base):
    __tablename__ = "permissions"
    __mapper_args__ = {"eager_defaults": True}

    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey("users.id", name="fk_permission_user_id", ondelete="CASCADE"), nullable=False)
    perm_name = Column(Text, nullable=False)
