from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database import crear_db
from usuarios import router

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

# INCLUIR ROUTER
app.include_router(router)

# CREAR BASE DE DATOS
@app.on_event("startup")
def on_startup():
    crear_db()

# PAGINA PRINCIPAL
@app.get("/")
def inicio(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )