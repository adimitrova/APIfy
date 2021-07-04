from fastapi import FastAPI

apify = FastAPI()

@apify.get('/')
async def root():
    return {"APIfy": "Welcome to APIfy. Upload your config here."}