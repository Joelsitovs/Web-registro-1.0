from fastapi import APIRouter
from conexion import db
from service.services import registrar_usuario , obtener_usuarios , obtener_usuario_dni, obtener_usuario_campo
from model.Modelo import Usuario



router = APIRouter()

@router.post("/registro")
def agregar_usuario(usuario: Usuario):
    return registrar_usuario(usuario)
  
  
@router.get("/usuarios")
def obtener_datos():
    return obtener_usuarios()

@router.get("/usuarios/{dni}")
def obtener_usuario(dni: str):
    return obtener_usuario_dni(dni)

@router.get("/usuarios/{campo}/{valor}")
def obtener_usuario_campo(campo: str, valor: str):
    return obtener_usuario_campo(campo, valor)



__all__ = ["router"]