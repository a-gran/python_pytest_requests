import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '993735695d6996dc045269871e0fe693'
HEADER = {
    "Content-Type": "application/json",
    "trainer_token": TOKEN
}
TRAINER_ID = '2402'

# Проверь, что ответ запрос GET /trainers приходит с кодом 200
def test_status_code():
    response_get_trainers = requests.get(url=f'{URL}/trainers')
    assert response_get_trainers.status_code == 200

#Проверь, что в ответе приходит строчка с именем твоего тренера
def test_get_my_trainer():
    response_get_my_trainer = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_get_my_trainer.json()["data"][0]["id"] == "2402"
