from fastapi import FastAPI,Request
from Models import Message
from getdata import GetData
from request_to_database import RequestTODataBase
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "WhatsApp"}


@app.post('/messages/send')
async def messages(dictionary: dict):
    objdata = GetData(dictionary)
    val_for_data_base = objdata.get_data()
    RequestTODataBase.insert_value(val_for_data_base)
    return {"message": "OK"}

@app.get('/messages/receive')
async def messages_receive():
    obj_row = RequestTODataBase()
    list_row = obj_row.request_select()
    return list_row

@app.get('/health')
async def check_health():
    return {'response': "200"}




