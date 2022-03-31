from typing import Any, Optional
from pydantic import BaseModel
import peewee
from pydantic.utils import GetterDict

class PeeweeGetterDict(GetterDict):
   def get(self, key: Any, default: Any = None):
      res = getattr(self._obj, key, default)
      if isinstance(res, peewee.ModelSelect):
         return list(res)
      return res

class UserRequestModel(BaseModel):
   username: str
   email: Optional[str] = None


class UserResponseModel(UserRequestModel):
   id: int
   class Config:
      orm_mode = True
      getter_dict = PeeweeGetterDict
