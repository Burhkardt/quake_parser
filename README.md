# Parser e API para relatório e ranking por log do jogo
Projeto criado para um teste de POO e API REST.
Este projeto tem a função de analizar o relatório de partida de Quake 3 e coletar as informações de abates, realizando também uma contagem dos pontos e a criação de um ranking. E com todos esses dados ele cria dois arquivos .json, "Ranking.json" e "Relatorio.json". E fazendo uso do FastAPI realizar a exibição dos dados

## Ferramentas usadas

Foram usadas as seguintes ferramentas:
```
Python 3.13.7
FastAPI
```

## Como executar o programa

Com o Python instalado, criar um venv *(opcional)* e instalar as dependências da API.
```python
python -m venv .venv
pip install fastapi uvicorn
```

Após a instalação das dependências, adicionar o arquivo "games.log", executar o comando para criação dos relatórios, e o comando para a inicialização do servidor.
```python
python parser.py
```
```bash
uvicorn api:app --reload
```
Após a inicialização do servidor, acessar o link http://127.0.0.1:8000/docs
Haverão duas opções de interação, Get Game, onde pegará partidas específicas pelo ID. **Caso queira a lista completa digitar 0**

E Get Rank, que ira apresentar o ranking de pontos de todos os jogadores registrados.