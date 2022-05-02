from lib2to3.pgen2 import token
from typing import Optional
from pydantic import BaseModel
from app.utils import PeeweeGetterDict

class LoginRequestModel(BaseModel):
   username: str
   password: str

class UserRequestModel(LoginRequestModel):
   email: Optional[str] = None
   first_name: Optional[str] = None
   last_name: Optional[str] = None
   phone: Optional[str] = None
   address: Optional[str] = None
   city: Optional[str] = None

class UserResponseModel(UserRequestModel):
   id: int
   is_active: Optional[bool] = False
   class Config:
      orm_mode = True
      getter_dict = PeeweeGetterDict

class LoginResponseModel(BaseModel):
   token: str
   user: UserResponseModel
   class Config:
      orm_mode = True
      getter_dict = PeeweeGetterDict

   