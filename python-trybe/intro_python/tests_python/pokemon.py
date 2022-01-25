import json


def retrieve_pokemons_by_type(type, reader):
    # lê o conteudo de reader e o transforma de json
    # para dicionário
    pokemons = json.load(reader)["results"]
    # filtra somente os pokemons do tipo escolhido
    pokemons_by_type = [
        pokemon for pokemon in pokemons if type in pokemon["type"]
    ]
    return pokemons_by_type

# --------------------------------------------------
# Segundo cenário onde a função espera o nome de um arquivo e a abertura do
# mesmo acontece dentro da função.


# import json


def retrieve_pokemons_by_type_cenario_2(type, filepath):
    with open(filepath) as file:
        pokemons = json.load(file)["results"]
        retrieve_pokemons_by_type_cenario_2 = [
            pokemon for pokemon in pokemons if type in pokemon["type"]
        ]
        return retrieve_pokemons_by_type_cenario_2
