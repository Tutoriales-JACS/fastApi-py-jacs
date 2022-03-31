
from typing import List
from fastapi import FastAPI, HTTPException
from database import User,database as conection
from schemas import UserRequestModel, UserResponseModel

app = FastAPI(
   title="Aplicación con FastAPI",
   description="FastAPI is a blazing fast, modern, and feature-rich open-source framework for building blazing fast APIs.",
   version="0.0.1"
)

@app.get("/", tags=["Public"])	
async def inicio():
   return {"Hello": "World"}

@app.get("/about", tags=["Public"])
async def acerca_de():
   return {"Hello": "World"}


# --------- User ----------
@app.get("/user", tags=["Usuario"], response_model=List[UserResponseModel])	
async def get_usuarios():
   return list(User.select())

@app.get("/user/{id}", tags=["Usuario"], response_model=UserResponseModel )	
async def get_usuario_id(id: int):
   user = User.filter(User.id == id).first()
   if user is None:
      raise HTTPException(404, "User not found")
   return user
      

@app.post("/user", 
      tags=["Usuario"], 
      response_model=UserResponseModel)	
async def save_usuarios(user: UserRequestModel):
   new_user = User.create(**user.dict())
   return new_user


@app.put("/user/{id}", tags=["Usuario"], response_model=UserResponseModel)	
async def update_usuarios(id: int,user: UserRequestModel):
   user_db = User.select().where(User.id == id).first()
   if user_db:
      user_db.username = user.username
      user_db.email = user.email
      user_db.save()
      return user_db
   else:
      raise HTTPException(404, "User not found")

@app.delete("/user/{id}", tags=["Usuario"])	
async def delete_usuarios(id: int):
   user = User.select().where(User.id == id).first()
   if user:
      user.delete_instance()
      return {"message": "El usuario ha sido eliminado"}
   else:
      raise HTTPException(404, "User not found")

# events
@app.on_event("startup")
def startup():
   if conection.is_closed():
      conection.connect()
   conection.create_tables([User])


@app.on_event("shutdown")
def shutdown():
   if not conection.is_closed():
      conection.close()