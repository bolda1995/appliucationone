from fastapi import FastAPI

app = FastAPI()
List_message = []
@app.get("/")
async def root():
    return {"message": "WhatsApp"}


@app.post('/messages/')
async def messages(message_json):
    print(message_json)
    return {"message": "message created successfully"}

@app.get('/messages/receive/')
async def messages_receive(meessage_id):
    print(meessage_id)
    return ""

@app.get('/health')
async def check_health():
    return {'response': "200"}




