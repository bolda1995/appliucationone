from fastapi import FastAPI,Request
from Models import Message

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "WhatsApp"}


@app.post('/messages/send')
async def messages(dictionary: dict):
    return {"message": "OK"}

@app.get('/messages/receive')
async def messages_receive():
    return {"detail": []}

@app.get('/health')
async def check_health():
    return {'response': "200"}




