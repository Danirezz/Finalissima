from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session

from database import engine, crear_db
from models import Usuario
from crud import crear_usuario, obtener_usuario

app = FastAPI()

# Templates
templates = Jinja2Templates(directory="templates")

# Archivos estaticos
app.mount("/static", StaticFiles(directory="static"), name="static")


# Crear DB al iniciar
@app.on_event("startup")
def on_startup():
    crear_db()


# Sesion DB
def get_session():
    with Session(engine) as session:
        yield session


# Inicio
@app.get("/")
def inicio(request: Request):

    usuarios = [
        {"nombre": "Ana"},
        {"nombre": "Carlos"}
    ]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "usuarios": usuarios
        }
    )


# Listar usuarios
@app.get("/usuarios")
def listar_usuarios():
    return ["usuario1", "usuario2"]


# Saludar usuario
@app.get("/usuarios/{nombre}")
def saludar_usuario(nombre: str):
    return {"mensaje": f"Hola {nombre}"}


# Crear usuario
@app.post("/usuarios")
def crear(
    usuario: Usuario,
    session: Session = Depends(get_session)
):
    return crear_usuario(usuario, session)


# Obtener usuario por ID
@app.get("/usuarios/id/{id}")
def obtener(
    id: int,
    session: Session = Depends(get_session)
):
    return obtener_usuario(id, session)