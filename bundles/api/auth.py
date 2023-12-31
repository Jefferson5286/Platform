from fastapi import APIRouter

from bundles.schemas.auth import AuthShema
from bundles.database import database


router = APIRouter(prefix='/auth')


@router.post('/register')
async def register(auth: AuthShema):

