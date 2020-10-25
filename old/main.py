from aiohttp import web
import aiohttp_jinja2
import jinja2
import os
import asyncio


async def pre_init(app):
    if os.environ.get('PROD', None) != 'true':
        app.add_routes([web.static('/static', 'static')])


@aiohttp_jinja2.template('index.html')
async def handler(request: web.Request):
    return {}


@aiohttp_jinja2.template('404.html')
async def handle_404(request):
    return {}

@aiohttp_jinja2.template('500.html')
async def handle_500(request):
    return {}


@web.middleware
async def error_middleware(request, handler):
    try:
        return await handler(request)
    except Exception as ex:
        code = 500
        if isinstance(ex, web.HTTPException):
            code = ex.status
        if code == 404:
            response = await handle_404(request)
        elif code == 500:
            response = await handle_500(request)
        else:
            raise ex
        response.set_status(code)
        return response


async def app_factory():
    app = web.Application(middlewares=[error_middleware])
    app.router.add_get('/', handler)
    await pre_init(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./templates'))
    return app


if __name__ == '__main__':
    web.run_app(app_factory())
