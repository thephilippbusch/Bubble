from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from typing import Dict

from server.auth.auth_bearer import JWTBearer
from server.auth.auth_handler import signJWT
from server.auth.user_sign_schema import UserSignSchema

from server.database.database import init_db

SERVER_ENV = config("SERVER_ENV")

# Can be changed to adapt to production behavior such as nginx configurations
root_path = "/"
if SERVER_ENV == "production":
  root_path = "/"

app = FastAPI(
  title="Bubble FastAPI Server", 
  version="1.0.0", 
  root_path=root_path
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.post("/auth/sign", tags=["auth"])
async def sign_api_key(user_sign: UserSignSchema = Body(...)) -> Dict:
  try:
    print(user_sign)
    return {}
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

@app.get("/", tags=["Hello World"])
async def hello_world() -> Dict:
  try:
    return {
      "successful": True,
      "message": "Hello World"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }