import json
class Game:
    def __init__(self, num_partida):
        self.partida = f"Game_{num_partida}"
        self.total_kills = 0
        self.players = set()
        self.kills = {}

    def add_player(self, nome):
        if nome != "<world>":
            self.players.add(nome)
            if nome not in self.kills:
                self.kills[nome] = 0

    def count_kills(self, killer, victim):
        self.total_kills += 1
        self.add_player(victim)
        if killer == "<world>":
            self.kills[victim] -= 1
        else:
            self.add_player(killer)
            self.kills[killer] += 1

    def dict_converter(self):
        return {
            "total_kills": self.total_kills,
            "players": list(self.players),
            "kills": self.kills
            }
    

class Parser:
    def __init__(self, diretorio):
        self.diretorio = diretorio
        self.partidas = {}

    def leitor(self):
        game_number = 0
        with open(self.diretorio, 'r') as log:
            for l in log:
                linha_tratada = l.strip()
                if "InitGame" in linha_tratada:
                    game_number += 1
                    game = Game(game_number)
                    self.partidas[game.partida] = game
                elif "Kill" in linha_tratada:
                    kill_text = l.split(":")[3]
                    killer = kill_text.split("killed")[0].strip()
                    victim = kill_text.split("killed")[1].split("by")[0].strip()
                    game.count_kills(killer, victim)

    def gera_relatorio(self, jsonlog_name="Relatorio.json"):
        log_formatado = {}
        for name, game in self.partidas.items():
            log_formatado[name] = game.dict_converter()
        with open(jsonlog_name, "w") as saida:
            json.dump(log_formatado, saida, indent = 4)
        print("Relatório gerado")

    def gera_ranking(self, jsonlog_name = "Ranking.json"):
        ranking = {}
        for games in self.partidas.values():
            for player, pontos in games.kills.items():
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
teste = Parser('games.log')
teste.leitor()
teste.gera_ranking()