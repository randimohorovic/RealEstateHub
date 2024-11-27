# Instrukcije za backend i frontend


## Backend:
1. **Conda env:**
```bash
   conda create --name realestatehub python=3.13
```

```bash
   conda activate realestatehub 
```
1. **Requirements.txt obavezno:**

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

