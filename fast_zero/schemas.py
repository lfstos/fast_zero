from pydantic import BaseModel, EmailStr


# Valida a Entrada/Saída, precisa ser uma str
class Message(BaseModel):
    message: str


# Modelo para validação Entrada/Saída de dados e documentação
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: str


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
