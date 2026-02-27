a = "2:00 Kill: 1022 3 22: <world> killed Isgalamido by MOD_TRIGGER_HURT"


def add_dict(num_partida):
    partidas = {
        f"Game_{num_partida}": {
            "total_kills": 0,
            "players": set(),
            "kills": {}
        }
    }
    return partidas

print(add_dict(3))

print(a.split(":")[3])
'''with open('games.log', 'r') as log:
    for l in log:
        if "kill" in l:
            texto_morte= l.split(":")[3]
            assassino = texto_morte.split("killed")[0]
            morte = texto_morte.split("killed")[1]
            morto = morte.split("by")[0]
            print(f"Assassino: {assassino}")
            print(f"Morto: {morto}")'''

teste = {"Escolhas":{
    "PessoaA":"Macarrão",
    "PessoaB":"peixe"
}}
print(teste)
teste.update({"PessoaC":"Feijão"})
print(teste)
teste.popitem()
print(teste)