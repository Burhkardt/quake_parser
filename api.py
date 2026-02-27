from fastapi import FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
import json

app = FastAPI(title = "Relatório e Ranking Quake", description="API para visualização de dados de partidas de Quake 3", docs_url=None, version="1.0.0")

try:
    with open("Relatorio.json", "r") as relatorio:
        log = json.load(relatorio)
        
except FileNotFoundError:
    print("Arquivo não encontrado.")

try:
    with open("Ranking.json", "r") as ranking:
        rank = json.load(ranking)

except FileNotFoundError:
    print("Arquivo não encontrado.")

@app.get("/docs", include_in_schema=False)
def custom_html():

    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title = app.title + " -Custom",
    )

@app.get("/partidas/{id}")
def get_game(id: int):
    game_name = f"Game_{id}"

    try:
        if id == 0:
            return log
        
        elif game_name in log:
            return {game_name: log[game_name]}
        
    except:
        pass

    raise HTTPException(status_code=404, detail="Partida não encontrada")
@app.get("/Rank/")
def get_rank():
    try:
        return rank
    except:
        pass
    raise HTTPException(status_code=404, detail="Ranking não encontrado")