from typing import Any, List, Optional
from datetime import date, datetime, time, timedelta
from typing import Optional
from uuid import UUID
from peewee import BlobField, IntegerField
import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res

class UsuarioModel(BaseModel):
    idUsuario:int
    Nombre:str
    ApellidoPaterno:str
    ApellidoMaterno:str
    FechaNacimiento:date
    Email:str
    NombreUsuario:str
    Password:str
    idTipoUsuario:int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
        validate_assignment = True