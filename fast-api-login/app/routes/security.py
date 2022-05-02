from fastapi import APIRouter, HTTPException, Header
from app.models import User, Token
from app.schemas import LoginRequestModel, LoginResponseModel
import uuid

router = APIRouter(
   prefix="/security",
   tags=["Seguridad"],
   responses={404: {"description": "No encontrado"}}
)

@router.post("/login", 
   response_model=LoginResponseModel, 
   description="Inicio de Sesión")
def iniciar_sesion(user: LoginRequestModel):
   user_md = User.get_or_none(User.username == user.username)
   if user_md is None:
      raise HTTPException(status_code=400,detail="Usuario no existe")
   if user_md.password != user.password:
      raise HTTPException(status_code=400, detail="Contraseña incorrecta")
   token_md = Token.get_or_none(Token.user == user_md)
   if token_md is None:
      token_md = Token.create(user=user_md, token=str(uuid.uuid4())+"."+str(user_md.id))
   return token_md



@router.post("/logout")
def cerrar_sesion(token: str=Header(None)):
   token_md = Token.get_or_none(Token.token == token)
   if token_md is None:
      raise HTTPException(status_code=400, detail="Token no existe")
   token_md.delete_instance()
   return {"message": "Sesión cerrada"}