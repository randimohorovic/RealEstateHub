from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uuid
import base64
import boto3
from botocore.exceptions import NoCredentialsError
import pandas as pd
from scraper.scraper import scrape_mondo_listings
from scraper.scraper2 import scrape_njuskalo_listings

app =FastAPI()
#ovo mi omogućuje da front end radi na localhost:3000 i komunicira
#sa backendom koji radi na http://localhost:8000/
app.add_middleware(
    CORSMiddleware,
     allow_origins=[
        "http://localhost",       
        "http://localhost:8000",  
        "http://localhost:3000"   
    ],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# DynamoDB 
dynamodb = boto3.resource("dynamodb", region_name="eu-north-1")
#table_name = "RealEstateListings" netreba mi vise, podjelio sam 2 table za svaku stranicu
#table = dynamodb.Table(table_name)
table_mondo =dynamodb.Table("MondoListings")
table_njuskalo =dynamodb.Table("NjuskaloListings")

def save_to_dynamodb(table, listings):
    for listing in listings:
        try:
            response = table.put_item(Item=listing)
            print(f"PutItem response: {response}")  
        except Exception as e:
            print(f"Error {listing}: {e}")


# mondo nekretnine 
@app.get("/listings")
async def scrape_and_fetch(url: str, max_pages: int = 1):
    try:
        listings = scrape_mondo_listings(url, max_pages)
        save_to_dynamodb(table_mondo, listings)

        response = table_mondo.scan()

        return {"status": "success", "podaci": response.get("Items", [])}
    except NoCredentialsError:
        raise HTTPException(status_code=500, detail="AWS credentials not configured.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    #njuskalo nektretnine
@app.get("/njuskalo-listings")
async def scrape_and_fetch_njuskalo(url: str, max_pages: int = 1):
    try:
        # scrrejpam listings i spremam
        listings = scrape_njuskalo_listings(url, max_pages)
        
        #spremi podatke u bazu
        save_to_dynamodb(table_njuskalo, listings)

        # fetcham podatke iz baze
        response = table_njuskalo.scan()

        return {"status": "success", "podaci": response.get("Items", [])}
    except NoCredentialsError:
        raise HTTPException(status_code=500, detail="AWS credentials not configured.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/root")
async def root():
    return {"message": "Welcome to RealEstateHub "}

