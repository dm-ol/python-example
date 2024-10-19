from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])
if __name__ == '__main__':
    web.run_app(app)

# Тут створюється веб-додаток через aiohttp.web.Application, додаються маршрути для обробки запитів до кореневої URL-адреси (/) та URL-адреси з ім'ям (/{name}).

# Функція handle обробляє запити, отримує ім'я з параметрів запиту (або використовує значення за умовчанням "Anonymous") та повертає відповідь з текстом привітання.
