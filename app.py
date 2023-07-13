import templates as templates
from fastapi import FastAPI,Request
from getdata import GetData
from request_to_database import RequestTODataBase
from logging_app import *
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/")
def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/messages/send')
async def messages(dictionary_data: dict):
    logging.info("Post endpoint was called.")
    objdata = GetData(dictionary_data)
    val_for_data_base, bool = objdata.get_data()
    if bool:
        mess_id = objdata.get_list_data(val_for_data_base)
        objval = RequestTODataBase()
        objval.alter_request_for_database(mess_id)
        return {"result": "success"}
    objval = RequestTODataBase()
    objval.insert_value(val_for_data_base)
    logging.info("Post endpoint called and return 200.")
    return {"result": "success"}

@app.get('/messages/receive')
async def messages_receive(request: Request):
    logging.info("get endpoint was called.")
    system = request.headers['receiver-system']
    obj_row = RequestTODataBase()
    list_row = obj_row.request_select(str(system))
    logging.info("get endpoint was called and return 200.")
    return {"Messages": list_row}

@app.get('/health')
async def check_health():
    return {'response': "200"}

app.add_middleware(LoggingMiddleware)

