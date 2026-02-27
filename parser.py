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
                if "initGame" in linha_tratada:
                    game_number += 1
                    game = Game(game_number)
                    self.partidas[game.partida] = game
                elif "Kill" in linha_tratada:
                    kill_text = l.split(":")[3]
                    killer = kill_text.split("killed")[0].strip()
                    victim = kill_text.split("killed")[1].split("by")[0].strip()
                    game.count_kills(killer, victim)
