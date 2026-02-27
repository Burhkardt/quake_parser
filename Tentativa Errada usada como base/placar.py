import json
def add_dict(num_partida):
    partidas = {
        f"Game_{num_partida}": {
            "total_kills": 0,
            "players": set(),
            "kills": {}
        }
    }
    return partidas
    

def leitura_log():
    with open('games.log', 'r') as log:
        full_log = dict()
        num_partida = 1
        game={}
        partida = f"Game_{num_partida}"
        for linha in log:
            linha_tratada = linha.strip()
            if "InitGame" in linha_tratada:
                game = add_dict(num_partida)
                partida = f"Game_{num_partida}"
                num_partida += 1
            elif "Kill" in linha_tratada:
                game[partida]["total_kills"] += 1
                texto_morte= linha.split(":")[3]
                assassino = texto_morte.split("killed")[0].strip()
                morte = texto_morte.split("killed")[1]
                morto = morte.split("by")[0].strip()
                game[partida]["players"].add(morto)
                if morto not in game[partida]["kills"]:
                    game[partida]["kills"][morto] = 0
                if assassino == "<world>":
                    game[partida]["kills"][morto] -= 1
                else:
                    game[partida]["players"].add(assassino)
                    if assassino not in game[partida]["kills"]:
                        game[partida]["kills"][assassino] = 0
                    game[partida]["kills"][assassino] += 1
            full_log.update(game)
        for l in full_log.values():
            l["players"] = list(l["players"])
        with open("Relatorio.json", "w") as saida:
            json.dump(full_log, saida, indent=4)
        for l in full_log.items():
            print(f"{l}\n")
        print("Relatório criádo com sucesso!")
        gera_ranking(full_log)
        

def gera_ranking(log:dict):
    ranking = {}
    for jogo, itens in log.items():
        for player, pontos in itens["kills"].items():
            if player not in ranking:
                ranking[player] = 0
            ranking[player] += pontos
    posicoes = dict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))
    n=1
    with open("Ranking.json", "w") as saida:
        json.dump(posicoes, saida, indent=4)
    for player, pontos in posicoes.items():
        print(f"{n}: {player} com um total de {pontos} kills")
        n+=1
    print("Ranking gerado com sucesso")
leitura_log()