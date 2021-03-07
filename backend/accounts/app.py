from aiohttp import web
from . import db_helper
from . import users


async def index(request):
    return web.Response(text="Welcome home!")


async def register(request):
    pass


async def init(config):
    app = web.Application()

    # Configure routes
    app.router.add_get('/', index)

    # save config
    app['config'] = config

    # Setup database
    db = db_helper.Database(app['config'])
    await db.init()

    userset = users.Users(db)
    await userset.init()
    await userset.register('asdsa', '1234', 'asdas@asda.as')
    await userset.register('aasdsdsa', '1234', 'asadas@asda.as')
    await userset.register('asdsa', '1234', 'asadas@asda.as')

    return app
