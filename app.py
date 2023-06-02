from fastapi import FastAPI
from Models import Message

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "WhatsApp"}


@app.post('/messages/send')
async def messages(message: Message):
    return {"message": "OK"}

@app.get('/messages/receive/')
async def messages_receive(meessage: Message):
    return {"detail": "ok"}

@app.get('/health')
async def check_health():
    return {'response': "200"}




