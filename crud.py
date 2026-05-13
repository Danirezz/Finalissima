from fastapi import HTTPException
from sqlmodel import Session

from models import Usuario


def crear_usuario(usuario: Usuario, session: Session):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


def obtener_usuario(id: int, session: Session):
    usuario = session.get(Usuario, id)

    if not usuario:
        raise HTTPException(status_code=404, detail="No encontrado")

    return usuario