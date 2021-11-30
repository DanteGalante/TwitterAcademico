from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from routers import usuario
from database import *
from peewee import *

app = FastAPI(title='Twitter Académico', description='API para Twitter', version='0.1')
app.include_router(usuario.router_usuarios)

@app.on_event("startup")
async def startup():
    if conn.is_closed():
        conn.connect()
        print("Se conecto")


@app.on_event("shutdown")
async def shutdown():
    print("Se cerró la conexión...")
    if not conn.is_closed():
        conn.close()

@app.on_event("startup")
async def startup():
    print("Connecting...")

@app.get("/")
async def root():
    return {"message": "Ya está lo del servidor banda!"}