from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid
import base64

app = FastAPI()

#trenutne sesije u memoriji, treba sa dynamodb zamjenit ??
sessions = {}

class LoginRequest(BaseModel):
    username: str
    password: str

#privremni data, treba baza spremit
real_estate_listings = [
    {"id": 1, "name": "Apartman Pula", "price": 1200, "location": "Pula"},
    {"id": 2, "name": "Apartman Rovinj", "price": 850, "location": "Rovinj"},
]

@app.post("/login")
async def login(login: LoginRequest):
    # login usera, ko sa nastave primejr samo da vidim da radi
    if login.username == "user" and login.password == "password":
        session_id = base64.b64encode(uuid.uuid4().bytes).decode("utf-8")
        sessions[session_id] = {"username": login.username}
        return {"status": "ok", "session_id": session_id}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/listings")
async def get_listings(session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"listings": real_estate_listings}
