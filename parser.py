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