from aiohttp import web
import aiohttp_jinja2
import jinja2
import os
import asyncio

app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./templates'))

if os.environ.get('PROD', None) == 'true':
    PROD = True
else:
    PROD = False
    app.add_routes([web.static('/static', './static')])


@aiohttp_jinja2.template('index.html')
async def handler(request: web.Request):
    return {}


app.add_routes([web.get('/', handler)])
web.run_app(app)
