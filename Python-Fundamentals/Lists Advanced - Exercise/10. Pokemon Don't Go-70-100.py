pokemons = [int(i) for i in input().split()]
removed = 0

while len(pokemons) > 0:
    pokemon_index = int(input())
    if pokemon_index >= len(pokemons):
        removed += pokemons[-1]
        pokemons = [i + pokemons[0] for i in pokemons]
        pokemons.pop(-1)
        pokemons.append(pokemons[0])
    elif pokemon_index < 0:
        removed += pokemons[0]
        pokemons[0] = pokemons[-1]
        pokemons.pop(-1)
    else:
        current = pokemons[pokemon_index]
        pokemons.pop(pokemon_index)
        for i in range(len(pokemons)):
            if pokemons[i] <= current:
                pokemons[i] += current
            else:
                pokemons[i] -= current
        removed += current
    print(pokemons)


print(removed)
