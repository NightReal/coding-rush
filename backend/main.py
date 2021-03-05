from aiohttp import web


async def index(request):
    return web.Response(text="Welcome home!")


async def backend_app():
    app = web.Application()
    app.router.add_get('/', index)
    return app


if __name__ == '__main__':
    web.run_app(backend_app(), port=8000)
