from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_PATH = "files/Relatorio_cadop.csv"

df = pd.read_csv(
    CSV_PATH,
    delimiter=";",
    encoding="latin-1",
    dtype=str
).fillna("").applymap(lambda x: x.strip() if isinstance(x, str) else x)

df.columns = df.columns.str.strip()

print(df.columns.tolist())

class SearchRequest(BaseModel):
    coluna: str = None
    valor: str = None

def buscar_no_csv(coluna: str = None, valor: str = None):
    if coluna and valor:

        resultados = df[df[coluna].str.contains(valor.strip(), na=False, case=False, regex=True)]

        return resultados.to_dict(orient="records")
    
@app.post("/buscar")
async def buscar(request: SearchRequest):
    return buscar_no_csv(request.coluna, request.valor)
