from typing import List
from fastapi import APIRouter, HTTPException
from app.schemas import UserRequestModel, UserResponseModel
from app.models import User

router = APIRouter(
   prefix="/users",
   tags=["Usuarios"],
   responses={404: {"description": "No encontrado"}}
)

@router.get("/", response_model=List[UserResponseModel])
def lista_usuarios():
   return list(User.select())


@router.post("/", response_model=UserResponseModel)
def crear_usuario(user: UserRequestModel):
   return User.create(**user.dict())

@router.put("/{id}", response_model=UserResponseModel)
def actualizar_usuario(id: int, user: UserRequestModel):
   user_md = User.get_or_none(User.id == id)
   if user_md is None:
      raise HTTPException(status_code=400, detail="Usuario no existe")
   User.update(**user.dict()).where(User.id == id).execute()
   user_md = User.get(User.id == id)
   return user_md

@router.delete("/{id}")
def eliminar_usuario(id: int):
   user_md = User.select().where(User.id == id).first()
   if user_md:
      user_md.delete_instance()
      return {"message": "Usuario eliminado"}
   else:
      raise HTTPException(status_code=400, detail="Usuario no existe")