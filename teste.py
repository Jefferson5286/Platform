from motor import motor_asyncio
from decouple import config
from asyncio import get_event_loop

_PASSWORD = config('mongodb.PASSWORD')
_USERNAME = config('mongodb.USERNAME')

_credentials = f'mongodb+srv://{_USERNAME}:{_PASSWORD}@platform.lsbpbpc.mongodb.net/?retryWrites=true&w=majority'

clinet = motor_asyncio.AsyncIOMotorClient(_credentials)


async def query():
    database = clinet.get_database('platform')
    collection = database.get_collection('user')

    data = collection.find_one({'nome': 'Jefferson'})

    print(data)


if __name__ == '__main__':
    from asyncio import run

    run(query())
