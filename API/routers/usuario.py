import datetime
from typing import List
from fastapi import APIRouter
from peewee import BlobField
from starlette.responses import Response
from models.usuario import create_usuario, list_usuarios, delete_usuario
from schemas import UsuarioModel


router_usuarios = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router_usuarios.get("/", response_model=List[UsuarioModel], summary="Lista de usuarios", description="Regresa todos los usuarios")
def get_usuarios():
    return list_usuarios()

@router_usuarios.post("/", response_model=UsuarioModel, summary="Crear un nuevo usuario")
async def create(Nombre:str ,ApellidoPaterno:str ,ApellidoMaterno:str ,FechaNacimiento:datetime.date ,Email:str ,NombreUsuario:str ,Password:str ,idTipoUsuario:int):
    return await create_usuario(Nombre=Nombre, ApellidoPaterno=ApellidoPaterno, ApellidoMaterno=ApellidoMaterno, FechaNacimiento=FechaNacimiento,
     Email=Email, NombreUsuario=NombreUsuario, Password=Password, idTipoUsuario=idTipoUsuario  )


@router_usuarios.delete(
    "/remove/{idUsuario}",
    summary="Eliminación de un usuario en específico",
    response_class=Response,
    responses={
        200: {"description": "Usuario eliminado exitosamente"},
        404: {"description": "Usuario no encontrado"},
    },
)
def remove_usuarios(idUsuario: int):
    del_usuario = delete_usuario(idUsuario)
    if del_usuario is None:
        return Response(status_code=404)
    return Response(status_code=200)