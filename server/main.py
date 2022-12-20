from fastapi import FastAPI, Body
from fastapi.params import Depends
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from typing import Dict

from server.auth.user_sign_schema import UserSignInSchema, UserSignUpSchema
from server.auth.auth_bearer import JWTBearer

from server.database.auth import Auth
from server.database.database import init_db
from server.database.list import List
from server.database.entries import Entries

from server.schemas.lists import CreateListSchema, UpdateListSchema
from server.schemas.entries import CreateEntrySchema, UpdateEntrySchema

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

# Auth Endpoints
@app.post("/auth/sign_in", tags=["Auth"])
async def sign_in(user_sign_in: UserSignInSchema = Body(...)) -> Dict:
  try:
    res = Auth.sign_in(username=user_sign_in.username, password=user_sign_in.password)

    if res is not None:
      return res

    return {
      "successful": False,
      "error": "User could not be signed in!"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

@app.post("/auth/sign_up", tags=["Auth"])
async def sign_in(user_sign_up: UserSignUpSchema = Body(...)) -> Dict:
  try:
    res = Auth.sign_up(
      username=user_sign_up.username,
      name=user_sign_up.name,
      surname=user_sign_up.surname,
      password=user_sign_up.password
    )

    if res is not None:
      return res

    return {
      "successful": False,
      "error": "User could not be signed in!"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

# List Endpoints
@app.get("/list/get_list_by_id", tags=["List"], dependencies=[Depends(JWTBearer())])
async def get_list_by_id(lid: str) -> Dict:
  try:
    db_result = List.get_list_by_id(lid)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": "No list was found"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

@app.get("/list/search_list", tags=["List"], dependencies=[Depends(JWTBearer())])
async def search_list(query: str) -> Dict:
  try:
    db_result = List.search_list(query_string=query)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": "No list was found"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

@app.get("/list/get_lists_by_user", tags=["List"], dependencies=[Depends(JWTBearer())])
async def get_lists_by_user(uid: str) -> Dict:
  try:
    db_result = List.get_user_lists(uid=uid)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": f"No lists were found for user {uid}"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

@app.post("/list/create_list", tags=["List"], dependencies=[Depends(JWTBearer())])
async def create_list(payload: CreateListSchema) -> Dict:
  try:
    db_result = List.create_list(title=payload.title, uid=payload.uid)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": "List could not be created!"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }
  
@app.put("/list/update_list", tags=["List"], dependencies=[Depends(JWTBearer())])
async def update_list(payload: UpdateListSchema) -> Dict:
  try:
    db_result = List.update_list(lid=payload.lid, title=payload.title)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": "No lists were found"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

@app.delete("/list/delete_list", tags=["List"], dependencies=[Depends(JWTBearer())])
async def delete_list(lid: str) -> Dict:
  try:
    db_result = List.remove_list(lid=lid)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": "No lists were found"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

# Entries Endpoints
@app.get("/entries/get_entry_by_id", tags=["Entries"], dependencies=[Depends(JWTBearer())])
async def get_entry_by_id(eid: str) -> Dict:
  try:
    db_result = Entries.get_entry_by_id(eid)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": "No entry was found"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

@app.get("/entries/search_entries", tags=["Entries"], dependencies=[Depends(JWTBearer())])
async def search_entries(query: str) -> Dict:
  try:
    db_result = Entries.search_entries(query_string=query)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": "No entry was found"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

@app.get("/entries/get_entries_by_list", tags=["Entries"], dependencies=[Depends(JWTBearer())])
async def get_entries_by_list(lid: str) -> Dict:
  try:
    db_result = Entries.get_list_entries(lid=lid)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": f"No entries were found for list {lid}"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

@app.post("/entries/create_entry", tags=["Entries"], dependencies=[Depends(JWTBearer())])
async def create_entry(payload: CreateEntrySchema) -> Dict:
  try:
    db_result = Entries.create_entry(name=payload.name, lid=payload.lid)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": "Entry could not be created!"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }
  
@app.put("/entries/update_entry", tags=["Entries"], dependencies=[Depends(JWTBearer())])
async def update_entry(payload: UpdateEntrySchema) -> Dict:
  try:
    db_result = Entries.update_entry(eid=payload.eid, name=payload.name)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": "List could not be removed!"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

@app.delete("/entries/delete_entry", tags=["Entries"], dependencies=[Depends(JWTBearer())])
async def delete_entry(eid: str) -> Dict:
  try:
    db_result = Entries.remove_entry(eid=eid)

    if db_result is not None:
      return db_result

    return {
      "successful": False,
      "message": "Entry could not be removed!"
    }
  except Exception as e:
    print(e)
    return {
      "successful": False,
      "error": str(e)
    }

