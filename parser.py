class Game:
    def __init__(self, num_partida):
        self.partida = f"Game_{num_partida}"
        self.total_kills = 0
        self.players = set()
        self.kills = {}
