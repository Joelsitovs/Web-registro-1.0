from model.Modelo import Usuario
from conexion import db

def registrar_usuario(usuario: Usuario):
    doc_ref = db.collection("usuarios").document(usuario.dni)
    doc_ref.set(usuario.dict())
    
   # doc_ref.set({"nombre": usuario.nombre, "dni": usuario.dni, "email": usuario.email, "fecha_nacimiento": usuario.fecha_nacimiento, "edad": usuario.edad})
    return {"message": "Usuario Registrado", "usuario": usuario.dict()}


def obtener_usuarios():
    usuarios = db.collection("usuarios").stream()
    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append(usuario.to_dict())
    return lista_usuarios



def obtener_usuario_dni(dni: str):
    doc_ref = db.collection("usuarios").document(dni)
    usuario_dni = doc_ref.get()
    return usuario_dni.to_dict()

def obtener_usuario_campo(campo: str, valor: str):
    usuarios = db.collection("usuarios").where(campo, "==", valor).stream()
    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append(usuario.to_dict())
    return lista_usuarios