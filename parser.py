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
    
                