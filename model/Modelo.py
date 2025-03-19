from pydantic import BaseModel , field_validator ,ValidationError
from datetime import datetime

class Usuario(BaseModel):
    nombre: str
    dni : str
    email: str
    fecha_nacimiento: str
    
    
    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls,nombre: str):
        if len(nombre) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        return nombre
    
    @field_validator("email")
    @classmethod
    def validar_email(cls,email: str):
        if "@" not in email or "." not in email:
            raise ValueError("El email debe ser valido")
        return email
    
    @field_validator("dni")
    @classmethod
    def validar_dni(cls,dni: str):
        if len(dni) != 9:
            raise ValueError("El DNI debe tener 8 caracteres")
        return dni
    
    @field_validator("fecha_nacimiento")
    @classmethod
    def validar_fecha_nacimiento(cls,fecha_nacimiento: str):
        try:
            datetime.strptime(fecha_nacimiento, "%Y/%m/%d")
        except ValueError:
            raise ValueError("La fecha debe tener el formato YYYY/MM/DD")
        return fecha_nacimiento


__all__ = ["Usuario"]