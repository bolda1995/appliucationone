from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse, RedirectResponse
from getdata import GetData
from request_to_database import RequestToDataBase
from logging_app import *
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from adminfunction.adminmodel import LoginRequest
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import traceback
from metrics import update_uptime
from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/login")
async def login(login_request: LoginRequest):
    # Получение логина и пароля из запроса
    username = login_request.username
    password = login_request.password

    # Проверка логина и пароля
    if username == "admin" and password == "password":
        return JSONResponse(content={"result": True})

    return JSONResponse(content={"result": False})
@app.get("/admin")
async def admin(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

@app.post('/messages/send')
async def messages_send(dictionary_data: dict):

    logging.info("Post endpoint was called.")
    objdata = GetData(dictionary_data)
    val_for_data_base, boolelement = objdata.get_data()

    objval = RequestToDataBase()

    if boolelement:
        mess_id = objdata.get_list_data(val_for_data_base)
        objval.alter_request_for_database(mess_id)
    else:
        objval.insert_value(val_for_data_base)

    logging.info("Post endpoint called and returned 200.")
    return {"result": "success"}

Instrumentator().instrument(app).expose(app)

@app.get('/messages/receive')
async def messages_receive(request: Request):
    system = request.headers.get('receiver-system')
    if not system:
        raise HTTPException(status_code=400, detail="Receiver system not specified in query parameters")

    obj_row = RequestToDataBase()
    list_row = obj_row.request_select(str(system))
    print(list_row)
    logging.info("GET endpoint was called and returned 200.")
    return {"Messages": list_row}


@app.get("/metrics")
def metrics():
    update_uptime()

@app.get('/health')
async def check_health():
    return {'response': "200"}





app.add_middleware(LoggingMiddleware)
