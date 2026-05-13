from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.models import Usuario
from app.database import get_session

router = APIRouter()

# LISTAR USUARIOS
@router.get("/usuarios")
def listar_usuarios(session: Session = Depends(get_session)):

    usuarios = session.query(Usuario).all()

    return usuarios


# OBTENER USUARIO
@router.get("/usuarios/{id}")
def obtener_usuario(
    id: int,
    session: Session = Depends(get_session)
):

    usuario = session.get(Usuario, id)

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario


# CREAR USUARIO
@router.post("/usuarios")
def crear_usuario(
    usuario: Usuario,
    session: Session = Depends(get_session)
):

    session.add(usuario)

    session.commit()

    session.refresh(usuario)

    return usuario