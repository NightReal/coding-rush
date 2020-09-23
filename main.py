from aiohttp import web
import aiohttp_jinja2
import jinja2
import os
import asyncio


async def pre_init(app):
    if os.environ.get('PROD', None) == 'true':
        PROD = True
    else:
        PROD = False
        app.add_routes([web.static('/static', './static')])


@aiohttp_jinja2.template('index.html')
async def handler(request: web.Request):
    return {}


async def app_factory():
    app = web.Application()
    app.router.add_get('/', handler)
    await pre_init(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./templates'))
    return app
