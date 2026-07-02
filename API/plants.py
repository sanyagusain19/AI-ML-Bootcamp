import requests

API_KEY = "sk-ZCcf6a453bcd14ff118539"
BASE_URL = "https://perenual.com/api/v2/species-list"


# 🌿 Fetch plants from API
def fetch_plants(query="rose", page=1):
    try:
        params = {
            "key": API_KEY,
            "q": query,
            "page": page
        }

        response = requests.get(BASE_URL, params=params)

        if response.status_code != 200:
            return {
                "success": False,
                "error": f"API failed with status {response.status_code}"
            }

        data = response.json()

        plants = []

        for plant in data.get("data", []):
            plants.append({
                "id": plant.get("id"),
                "common_name": plant.get("common_name"),
                "scientific_name": plant.get("scientific_name"),
                "cycle": plant.get("cycle"),
                "watering": plant.get("watering"),
                "sunlight": plant.get("sunlight"),
                "family": plant.get("family")
            })

        return {
            "success": True,
            "query": query,
            "count": len(plants),
            "plants": plants
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


# 🌸 Fetch single plant detail
def fetch_plant_detail(plant_id):
    try:
        url = f"https://perenual.com/api/v2/species/details/{plant_id}"

        params = {
            "key": API_KEY
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return {
                "success": False,
                "error": "Plant not found"
            }

        return {
            "success": True,
            "data": response.json()
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
