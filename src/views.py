from aiohttp import web
import db


async def index(request):
    all_news = await db.get_all_news()
    return web.json_response(all_news)


async def create_news(request):
    new_news = await request.json()
    await db.create_news(new_news)
    try:
        print('JSON:', await request.json())
    except Exception as ex:
        print('JSON: ERROR:', ex)
    return web.Response(text='Received...')


async def get_all_news(request):
    all_news = await db.get_all_news()
    return web.json_response(all_news)


async def get_one_news(request):
    news_id = request.match_info.get('news_id')
    news = await db.get_news_by_id(int(news_id))
    return web.json_response(news)


async def update_news(request):
    news_id = request.match_info.get('news_id')
    new_news = await request.json()
    await db.update_news(news_id, new_news)
    return web.Response(text='Updated...')


async def delete_news(request):
    news_id = request.match_info.get('news_id')
    await db.delete_news(news_id)
    return web.Response(text='Deleted')

