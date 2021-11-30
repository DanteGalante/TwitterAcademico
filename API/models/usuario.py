from datetime import date, datetime
from peewee import *
from models.base import BaseModel
from peewee import BlobField, IntegerField


class Usuario(BaseModel):
    idUsuario = AutoField()
    Nombre = CharField(max_length=30)
    ApellidoPaterno  = CharField(max_length=30)
    ApellidoMaterno  = CharField(max_length=30)
    FechaNacimiento = DateField
    Email  = CharField(max_length=25)
    NombreUsuario = SmallIntegerField()
    Password = CharField(max_length=30)
    idTipoUsuario = IntegerField

    class Meta:
        db_table = 'usuario'

async def create_usuario(Nombre:str, ApellidoPaterno:str, ApellidoMaterno:str, FechaNacimiento:date, Email:str, NombreUsuario:str, Password:str, idTipoUsuario:int):
    usuario_object = Usuario(
        Nombre=Nombre,
        ApellidoPaterno=ApellidoPaterno,
        ApellidoMaterno=ApellidoMaterno,
        FechaNacimiento=FechaNacimiento,
        Email=Email,
        NombreUsuario=NombreUsuario,
        Password=Password,
        idTipoUsuario=idTipoUsuario
    )
    usuario_object.save()
    return usuario_object

def list_usuarios(skip: int = 0, limit: int = 100):
    return list(Usuario.select().offset(skip).limit(limit))

def delete_usuario(idUsuario: int):
    return Usuario.delete().where(Usuario.idUsuario == idUsuario).execute()   