import asyncpg
from . import users


class Database:
    def __init__(self, settings):
        self.settings = settings

    async def init(self):
        self.conn = await asyncpg.connect(user=self.settings.POSTGRES_USER, password=self.settings.POSTGRES_PASSWORD, database=self.settings.POSTGRES_DB,
                                          host=self.settings.POSTGRES_HOST)
        await self._init_db()

    async def _init_db(self):
        script = open('schema.sql').read()
        try:
            async with self.conn.transaction():
                await self.conn.execute(script)
        except Exception as e:
            raise e

    async def create_user(self, email, username, hashed_password, activation_token):
        try:
            async with self.conn.transaction():
                await self.conn.execute("""
                    INSERT INTO users.users (email, username, hashed_password,  is_activated, activation_token)
                    VALUES                  (   $1,       $2,              $3,            $4,               $5)
                """, email, username, hashed_password, False, activation_token)
                return await self.conn.fetchval("""
                    SELECT max(id) FROM users.users;
                """)
        except Exception as e:
            raise e
