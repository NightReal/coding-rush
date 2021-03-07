from aiohttp import web
import accounts.app
import settings


async def index(request):
    return web.Response(text="Welcome home!")

async def init():
    app = web.Application()

    # Configure global app
    app['config'] = settings

    # Setup subapps coroutines
    app.add_subapp('/profile/', await accounts.app.init(settings))

    # Setup global routes
    app.router.add_get('/', index)

    return app


if __name__ == '__main__':
    web.run_app(init(), port=8000)
