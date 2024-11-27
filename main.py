from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid
import base64

app = FastAPI()

#ovo mi omogućuje da front end radi na localhost:3000 i komunicira
#sa backendom koji radi na http://localhost:8000/
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

#trenutne sesije u memoriji, treba sa dynamodb zamjenit ??
#sessions = {}

# class LoginRequest(BaseModel):
#     username: str
#     password: str

#privremni data cisto da vidim dali radi , treba baza spremit
real_estate_listings = [
    {"id": 1, "name": "Apartman Pula", "price": 1200, "location": "Pula"},
    {"id": 2, "name": "Apartman Rovinj", "price": 850, "location": "Rovinj"},
]

#mislim da login necu ni imati zapravo
# @app.post("/login")
# async def login(login: LoginRequest):
#     # login usera, ko sa nastave primejr samo da vidim da radi
#     if login.username == "user" and login.password == "password":
#         session_id = base64.b64encode(uuid.uuid4().bytes).decode("utf-8")
#         sessions[session_id] = {"username": login.username}
#         return {"status": "ok", "session_id": session_id}
#     raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/listings")
async def get_listings(): #(session_id: str)
    # hocu samo vratit podatke iz baze(trenutno iz lokalne) bez provjere sessiona

    return{"status": "uspjesno", "podaci":real_estate_listings}
    # if session_id not in sessions:
    #     raise HTTPException(status_code=401, detail="Unauthorized")
    # return {"listings": real_estate_listings}
