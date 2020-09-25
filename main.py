from aiohttp import web
import aiohttp_jinja2
import jinja2
import os
import asyncio


async def pre_init(app):
    if os.environ.get('PROD', None) != 'true':
        app.add_routes([web.static('/static', './static')])


@aiohttp_jinja2.template('index.html')
async def handler(request: web.Request):
    return {}


@aiohttp_jinja2.template('404.html')
async def handle_404(request):
    return {}


@web.middleware
async def error_middleware(request, handler):
    try:
        return await handler(request)
    except web.HTTPException as ex:
        if ex.status == 404:
            response = await handle_404(request)
        else:
            raise ex
        response.set_status(ex.status)
        return response


async def app_factory():
    app = web.Application(middlewares=[error_middleware])
    app.router.add_get('/', handler)
    await pre_init(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./templates'))
    return app
