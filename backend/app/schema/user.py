from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str
    password: str


class UserRetrieveSchema(BaseModel):
    username: str
