import io
import json
import hashlib
import asyncio
from aiohttp import web
from file_manager import FileManager

routes = web.RouteTableDef()
fm = FileManager()

@routes.get('/')
async def hello(request):
    print('get request:', request)
    return web.Response(text="Async File Storage")

@routes.post("/upload_file")
async def upload_file(request):
    print('get request:', request)
    result = await fm.upload_file(request)
    return web.Response(text=result)

@routes.get("/file/")
async def download_file(request):
    print('get request:', request)
    fm.download()
    return web.Response(text="Download File")

@routes.delete("/file/{idhash}/")
async def delete_file(request, idhash):
    print('get request:', request)
    fm.delete_file()
    return web.Response(text="Delete File")

app = web.Application()
app.add_routes(routes)
web.run_app(app,host='127.0.0.1',port=8080)