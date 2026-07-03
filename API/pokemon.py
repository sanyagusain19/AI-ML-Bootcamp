import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"
}

def fetch_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()

    abilities = [a['ability']['name'] for a in data['abilities']]
    types = [t['type']['name'] for t in data['types']]

    stats = {
        "hp": data["stats"][0]["base_stat"],
        "attack": data["stats"][1]["base_stat"],
        "defense": data["stats"][2]["base_stat"],
        "special_attack": data["stats"][3]["base_stat"],
        "special_defense": data["stats"][4]["base_stat"],
        "speed": data["stats"][5]["base_stat"]
    }

    return {
        "name": data["name"],
        "id": data["id"],
        "image": data["sprites"]["other"]["official-artwork"]["front_default"]
                 or data["sprites"]["front_default"],
        "types": types,
        "abilities": abilities,
        "stats": stats
    }