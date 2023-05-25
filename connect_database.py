import databases
import sqlalchemy
from fastapi import FastAPI
app = FastAPI()
database_url = "postgresql://user:password@localhost:5432/mydatabase"
database = databases.Database(database_url)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()