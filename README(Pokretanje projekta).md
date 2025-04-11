# Instrukcije za backend i frontend


## Backend:
1. **Conda env:**
```bash
   conda create --name realestatehub python=3.13
```

```bash
   conda activate realestatehub 
```
2. **Requirements.txt obavezno:**

```bash
   pip install -r requirements.txt
```

```bash
   uvicorn main:app --reload
```

```bash 
    #uvicorn main:app --reload (ako dode greska kao primjer ERROR:    [Errno 48] Address already in 
    #use onda --> lsof -i :8000 <-- (komanda prekida procese na toj adresi))
````

frontend: 

```bash
    cd frontend
```
```bash
    npm install
```
```bash
    npm start
```


### 3. Kreiraj `.env` datoteku

Preimenuj `.env.example` i nazovi ga `.env`:


### 4. Unesi svoje AWS podatke u `.env` 

Unutra dodaj:
```
AWS_ACCESS_KEY_ID=OVDJE_IDE_TVOJ_KLJUC
AWS_SECRET_ACCESS_KEY=OVDJE_IDE_TAJNI_KLJUC
AWS_REGION=eu-north-1
DYNAMODB_TABLE_NAME=RealEstateListings
```

> Ove podatke možeš dobiti od autora projekta 

### 5. Pokreni aplikaciju

Ako koristiš Docker:

```bash
docker-compose up --build
```
Nakon što se sve builda, aplikacija će biti dostupna na:

- Frontend: http://localhost
- Backend: http://localhost:8000
---

Ako ti što zapne, obrati se autoru projekta.

---


