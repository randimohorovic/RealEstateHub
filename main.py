from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid
import base64
import pandas as pd
from scraper.scraper import scrape_real_estate_listings 

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


#privremni data cisto da vidim dali radi , treba baza spremit
real_estate_listings = [
    {"id": 1, "name": "Apartman Pula", "price": 1200, "location": "Pula"},
    {"id": 2, "name": "Apartman Rovinj", "price": 850, "location": "Rovinj"},
]

@app.get("/listings")
async def get_listings(url: str, max_pages: int = 10):
    try:
        listings = scrape_real_estate_listings(url, max_pages=max_pages)
        return  {"status": "success", "podaci": listings}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/root")
async def root():
    return {"message": "Welcome to RealEstateHub API"}

