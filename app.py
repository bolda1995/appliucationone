from fastapi import FastAPI

app = FastAPI()
List_message = []
@app.get("/")
async def root():
    return {"message": "WhatsApp"}


@app.post('/messages/{message_json}')
async def messages(message_json):

    return {"message": "message created successfully"}

@app.get('/messages/receive/')
async def messages_receive(meesage_id, status, date_form, date_to):
    return ""

@app.get('/health')
async def check_health():
    return {'response': "200"}




