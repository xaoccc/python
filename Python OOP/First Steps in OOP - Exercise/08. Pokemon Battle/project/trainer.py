from project.pokemon import Pokemon

class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"
        
        
    def release_pokemon(self, pokemon_name: string):
        for pok in self.pokemons:
            if pok.name == pokemon_name:
                self.pokemons.remove(pok)
                return f"You have released {pokemon_name}"
        
        return "Pokemon is not caught"
        
        
    def trainer_data(self):
        output = f"Pokemon Trainer {self.name}\nPokemon count {len(pokemons)}"
        for pok in pokemons:
            output += f"\n- {pokemon.pokemon_details()}"
        return output
