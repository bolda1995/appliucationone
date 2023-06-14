from fastapi import FastAPI,Request
from getdata import GetData
from request_to_database import RequestTODataBase
from request_parse import *
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "WhatsApp"}


@app.post('/messages/send')
async def messages(dictionary_data: dict):
    objdata = GetData(dictionary_data)
    val_for_data_base = objdata.get_data()
    objval = RequestTODataBase()
    objval.insert_value(val_for_data_base)
    return {"result": "success"}

@app.get('/messages/receive')
async def messages_receive(request: Request):
    system = request.headers['receiver-system']
    obj_row = RequestTODataBase()
    list_row = obj_row.request_select(str(system))
    return {"Messages": list_row}

@app.get('/health')
async def check_health():
    return {'response': "200"}




