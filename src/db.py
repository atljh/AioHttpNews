import asyncio
import motor.motor_asyncio
import config


async def init_db():
    try:
        conn_str = config.conn_str
        client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
        db = client[config.mongo_db]
        return client, db
    except Exception as Exc:
        return f"Unable to connect to the server. {Exc}"


async def create_news(news_to_create):
    client, db = await init_db()
    collection = db[config.news_collection]
    result = await collection.insert_one()
    client.close()
    return result


async def get_all_news():
    client, db = await init_db()
    collection = db[config.news_collection]
    result = [new async for new in collection.find()]
    client.close()
    return result


async def get_news_by_id(news_id):
    client, db = await init_db()
    collection = db[config.news_collection]
    result = await collection.find_one({'_id': news_id})
    client.close()
    return result


async def update_news(news_id, new_news):
    client, db = await init_db()
    collection = db[config.news_collection]
    news_to_update = await get_news_by_id(news_id)
    result = await collection.update_one(news_to_update,
                                   {'$set': new_news}, upsert=False)
    client.close()
    return result


async def delete_news(news_id):
    client, db = await init_db()
    collection = db[config.news_collection]
    news_to_delete = get_news_by_id(news_id)
    result = await collection.delete_one(news_to_delete)
    client.close()
    return result


loop = asyncio.get_event_loop()
loop.run_until_complete(get_all_news())
