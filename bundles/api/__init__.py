from fastapi import APIRouter
from . import auth, query


api = APIRouter(prefix='/api')

api.include_router(query.router)
api.include_router(auth.router)
