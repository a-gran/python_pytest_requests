import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'a64b9fa06bf1159f0a649558ea12f3a3'
HEADER = {
    "Content-Type": "application/json",
    "trainer_token": TOKEN
}

body_create = {
    "name": "Наваратха",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change_name = {
    "pokemon_id": "28442",
    "name": "Махаратха",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}

body_add_pokeball = {
    "pokemon_id": "28442"
}

# создание покемона
response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)
print(response_create.status_code)
message = response_create.json()['message']
print(message)

# смена имени покемона
response_change_name = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change_name)
print(response_change_name.text)
print(response_change_name.status_code)

# поймать покемона в покебол
response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(response_add_pokeball.text)
print(response_add_pokeball.status_code)
