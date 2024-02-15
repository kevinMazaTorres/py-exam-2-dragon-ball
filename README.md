# Examen: funciones sobre Dragon Ball API

Usando la API de Dragon Ball (https://dragonball-api.com/api-docs), crea una serie de funciones que permitan obtener información de los personajes y planetas. (https://github.com/robinparadise/py-exam-2-dragon-ball).

- Enviar la solución (zip) como adjunto al email: **rgiles@metrodoraeducation.com**

La API de Dragon Ball tiene la siguiente estructura:

- https://dragonball-api.com/api/characters
  - /{id}
  - /{id}/transformations
- https://dragonball-api.com/api/planets
  - /{id}
- ?limit=10: limita el número de resultados

Crea una clase `DragonBallAPI`, `Character` y una clase `Planet` que permita manejar la información de los personajes y planetas respectivamente.

Aquí un ejemplo de cómo podría ser la implementación:

```python
import requests
import random

class Character:
  # def __str__(self):
  #   return self.name
  pass

class Planet:
  # def __str__(self):
  #   return self.name
  pass


class DragonBallAPI:
  def __init__(self):
    self.url = 'https://dragonball-api.com/api'

  def get_characters(self):
    pass

  def get_characters_names(self):
    pass

  ...

api = DragonBallAPI()
print(api.get_characters())
print(api.get_characters_names())
...

```

  - (1pts) Crea una función que liste solo los nombres de todos los personajes en la clase `DragonBallApi`
    - la funcion debe llamarse `get_characters_names()`
    - el total de personajes es 58

  - (1pts) funciones de filtrado en la clase `DragonBallApi`:
    - (0.5pts) Crea una función que liste solo los personajes por género
      - la funcion debe llamarse `get_characters_by_gender(gender)`
      - La función debe retornar solo los nombres de los personajes
    - (0.5pts) Crea una función que liste solo los personajes por raza
      - la funcion debe llamarse `get_characters_by_race(race)`
      - La función debe retornar solo los nombres de los personajes
  
  - (1pts) Crea un función que retorne una lista con todos los nombres de las transformaciones de un personaje. La función debe llamarse `character.get_transformations()` y debe usar la clase `Character`.
  
  - (2pts) funciones sobre /planets
    - (0.5pts) una funcion `get_planets()` que retorne una lista con los nombres de los planetas
    - (0.5pts) una función `get_destroyed_planets()` que retorne una lista con los nombres de los planetas destruidos
    - (1pts) Una funcion que retorne la lista de personajes de un planeta, la función debe llamarse `planet.get_characters()` y debe retornar solo los nombres de los personajes usando la clase `Planet`.
  

  - (2.5pts) Crea dos funciones en la clase `DragonBallApi`:
    - (1pts) `get_weakest()` un función que liste los personaje(s) con menos poder (maxKi 0).
    - (1.5pts) `get_strongest()` un función que liste los personaje(s) con más poder.
    **Nota: Un septillón es \(10^{24}\), lo que significa un 1 seguido de 24 ceros. Por otro lado, un googolplex es \(10^{10^{100}}\), que es un 1 seguido de un googol de ceros (Un googol es un 1 seguido de 100 ceros).**

    
  - (2.5pts) Haz que la suma de 2 personajes (`characters`) retorne un string con la suma parcial de los nombres. La sentencia se debe llamar `character1 + character2`, donde `character1` y `character2` son instancias de la clase `Character`. Ejemplo:
    
  ```python
    character1 = Character({'name': 'Goku'})
    character2 = Character({'name': 'Vegeta'})
    nombre = character1 + character2
    print(nombre) # Output: 'Gokugeta'

    character3 = Character({'name': 'Gohan'})
    character4 = Character({'name': 'Piccolo'})
    nombre = character3 + character4
    print(nombre) # Output: 'Gohacolo'

  ```

