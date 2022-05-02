from fastapi import FastAPI
from app.models import User, Token
from .routes import security, users
from . import db

def init_project()->FastAPI:
   app = FastAPI(
      title="API de Seguridad",
      description="Inicio de Sesión en FastAPI",
      version="0.0.1"
   )
   
   # evento del servidor
   @app.on_event("startup")
   async def startup():
      db.conect_db()
      db.database.create_tables([User, Token], safe=True)
   @app.on_event("shutdown")
   async def shutdown():
      db.disconnect_db()
   
   # rutas
   app.include_router(security.router)
   app.include_router(users.router)
   return app