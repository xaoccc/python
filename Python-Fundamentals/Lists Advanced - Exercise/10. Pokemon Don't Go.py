pokemons = [int(i) for i in input().split()]
removed = 0

while pokemons:
    pokemon_index = int(input())
    if pokemon_index >= len(pokemons):
        current = pokemons[-1]
        removed += pokemons[-1]
        pokemons[-1] = pokemons[0]

    elif pokemon_index < 0:
        current = pokemons[0]
        removed += pokemons[0]
        pokemons[0] = pokemons[-1]

    else:
        current = pokemons[pokemon_index]
        pokemons.pop(pokemon_index)
        removed += current

    for i in range(len(pokemons)):
        if pokemons[i] <= current:
            pokemons[i] += current
        else:
            pokemons[i] -= current

print(removed)
