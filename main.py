from fastapi import FastAPI
from bundles.api import api

app = FastAPI()
app.include_router(api)
