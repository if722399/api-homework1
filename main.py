from time import time
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Union

app = FastAPI()

class Users(BaseModel):

    user_name:str
    user_id: int
    user_email:str
    age: Union[int,None]=None
    recommendations: list[str]
    zip: Union[int,None]=None


user_dict = {}

@app.put('/users')
def create_post(user: Users):
    user = user.dict()

    if user['user_id'] in user_dict:
        raise ValueError(f'User {user["user_id"]} already exists')

    user_dict[user['user_id']] = user

    return {'Description':f'User creado correctamente {user["user_id"]}, su nombre es: {user["user_name"]}'}


@app.put('/users/update')
def update_user(user:Users):
    user = user.dict()

    if user['user_id'] not in user_dict:
        raise ValueError(f'User {user["user_id"]} does not exist')

    user_dict[user['user_id']] = user

    return {'Description':f'El user {user["user_id"]} con el nombre: {user["user_name"]} fue actualizado correctamente'}





if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", reload=True)

