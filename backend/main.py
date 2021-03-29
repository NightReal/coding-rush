from aiohttp import web
import settings
import db
from aiohttp_security import JWTIdentityPolicy
from aiohttp_security import setup as setup_security

from users.security import DBAuthorizationPolicy


async def index(request):
    return web.Response(text="Welcome home!")


async def init():
    app = web.Application()

    # Configure global app
    app['config'] = settings

    # Setup subapps coroutines
    pass

    database = db.Database(settings)
    await database.init()

    # security setup

    setup_security(app,
                   JWTIdentityPolicy(settings.SECRET_KEY),
                   DBAuthorizationPolicy(database))

    # Setup global routes
    app.router.add_get('/', index)

    return app


if __name__ == '__main__':
    web.run_app(init(), port=8000)
