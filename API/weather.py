import requests

url = "https://api.weather.com/v3/wx/forecast/daily/7day"
headers ={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"}


API_KEY = "71f92ea9dd2f4790b92ea9dd2f779061"

def fetch_weather(lat=30.13, lon=77.28):

    params = {
        "geocode": f"{lat},{lon}",
        "units": "m",
        "language": "en-IN",
        "format": "json",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    return response.json()
