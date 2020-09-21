import asyncio
from aiohttp import web
from file_manager import FileManager

routes = web.RouteTableDef()
fm = FileManager()

@routes.get('/')
async def hello(request):
    return web.Response(text="Async File Storage")

@routes.post("/upload_file")
async def upload_file(request):
    fm.upload_file()

@routes.get("/file/download")
async def download_file(request):
    fm.download()
    return web.Response(text="Download File")

@routes.delete("/file/delete")
async def delete_file(request):
    fm.delete_file()

app = web.Application()
app.add_routes(routes)
web.run_app(app,host='127.0.0.1',port=8080)