import requests
import json
token = 'fa8581156510e5f4a97335b4eb215a90'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Амбреон",
    "photo": "https://abrakadabra.fun/uploads/posts/2022-01/1642706272_15-abrakadabra-fun-p-pokemon-umbreon-33.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1336,
    "name": "Umbreon",
    "photo": "https://abrakadabra.fun/uploads/posts/2022-01/1642706272_15-abrakadabra-fun-p-pokemon-umbreon-33.png"
})

response_get = requests.get('https://pokemonbattle.me:5000/trainers/pokemons_in_pokeballs', params = {'trainer_id' : '1190'})
print(response_get.text)


response_put_second = requests.put('https://pokemonbattle.me:5000/trainers/deletePokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": 1336
})

print(response_put_second.text)