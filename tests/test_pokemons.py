import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'a64b9fa06bf1159f0a649558ea12f3a3'
HEADER = {
    "Content-Type": "application/json",
    "trainer_token": TOKEN
}
TRAINER_ID = '4281'

def test_status_code():
    response_get_pokemons = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_get_pokemons.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == "Бульбазавр"

@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '28442')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
