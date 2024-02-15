import requests

class DragonBallAPI:
    def __init__(self):
        self.base_url = "https://dragonball-api.com/api"

    def _make_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    def get_character_info(self, character_id):
        return self._make_request(f"characters/{character_id}")

    def get_character_transformations(self, character_id):
        return self._make_request(f"characters/{character_id}/transformations")

    def get_planet_info(self, planet_id):
        return self._make_request(f"planets/{planet_id}")

    def get_characters_names(self):
        characters_names = []
        for character_id in range(1, 59):  # El total de personajes es 58
            character_info = self.get_character_info(character_id)
            if character_info:
                characters_names.append(character_info["name"])
        return characters_names

    def get_characters_by_gender(self, genero):
        characters_by_gender = []
        for character_id in range(1, 59):
            character_info = self.get_character_info(character_id)
            if character_info and character_info.get("gender") == genero:
                characters_by_gender.append(character_info["name"])
        return characters_by_gender

    def get_characters_by_race(self, raza):
        characters_by_race = []
        for character_id in range(1, 59):
            character_info = self.get_character_info(character_id)
            if character_info and character_info.get("race") == raza:
                characters_by_race.append(character_info["name"])
        return characters_by_race

    def get_planets(self):
        planets_info = self._make_request("planets")
        return [planet["name"] for planet in planets_info]

    def get_destroyed_planets(self):
        destroyed_planets_info = self._make_request("planets/destroyed")
        return [planet["name"] for planet in destroyed_planets_info]

class Character:
    def __init__(self, character_id):
        api = DragonBallAPI()
        self.info = api.get_character_info(character_id)
        self.transformations = api.get_character_transformations(character_id)

    def get_info(self):
        return self.info

    def get_transformations(self):
        transformation_names = [transformation["name"] for transformation in self.transformations]
        return transformation_names

class Planet:
    def __init__(self, planet_id):
        api = DragonBallAPI()
        self.info = api.get_planet_info(planet_id)

    def get_info(self):
        return self.info

    def get_characters(self):
        characters_info = self.info.get("characters", [])
        return [character["name"] for character in characters_info]

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancia de la clase DragonBallAPI
    api = DragonBallAPI()

    # Obtener nombres de todos los personajes
    characters_names = api.get_characters_names()
    print("\nNombres de todos los personajes:")
    for name in characters_names:
        print(name)

    # Filtrar personajes por género (por ejemplo, "Male")
    male_characters = api.get_characters_by_gender("Male")
    print("\nPersonajes masculinos:")
    for name in male_characters:
        print(name)

    # Filtrar personajes por raza (por ejemplo, "Saiyan")
    saiyan_characters = api.get_characters_by_race("Saiyan")
    print("\nPersonajes de raza Saiyan:")
    for name in saiyan_characters:
        print(name)

    # Obtener nombres de todas las transformaciones de un personaje (por ejemplo, Goku)
    goku_transformations = Character(1).get_transformations()
    print("\nTransformaciones de Goku:")
    for transformation in goku_transformations:
        print(transformation)

    # Obtener nombres de todos los planetas
    planets_names = api.get_planets()
    print("\nNombres de todos los planetas:")
    for name in planets_names:
        print(name)

    # Obtener nombres de planetas destruidos
    destroyed_planets_names = api.get_destroyed_planets()
    print("\nNombres de planetas destruidos:")
    for name in destroyed_planets_names:
        print(name)

    # Obtener nombres de personajes en un planeta (por ejemplo, la Tierra)
    earth_characters = Planet(1).get_characters()
    print("\nPersonajes en la Tierra:")
    for name in earth_characters:
        print(name)
