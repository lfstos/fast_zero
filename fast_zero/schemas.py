from pydantic import BaseModel, EmailStr


# Valida a Entrada/Saída, precisa ser uma str
class Message(BaseModel):
    message: str


# Modelo para validação Entrada/Saída de dados e documentação
class UserSchema(BaseModel):
    print('UserSchema')
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    print('UserPublic')
    id: int
    username: str
    email: str


class UserDB(UserSchema):
    print('UserDB')
    id: int


class UserList(BaseModel):
    print('UserList')
    users: list[UserPublic]
