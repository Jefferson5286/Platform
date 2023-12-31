from motor import motor_asyncio
from decouple import config

_PASSWORD = config('mongodb.PASSWORD')
_USERNAME = config('mongodb.USERNAME')

_credentials = f'mongodb+srv://{_USERNAME}:{_PASSWORD}@platform.lsbpbpc.mongodb.net/?retryWrites=true&w=majority'

clinet = motor_asyncio.AsyncIOMotorClient(_credentials)

database = clinet.get_database('platform')
