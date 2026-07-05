#  API Integration Projects

A collection of Python projects demonstrating how to integrate and consume various public APIs. This folder showcases practical examples of fetching, processing, and manipulating data from different sources.

##  Table of Contents

- [Projects Overview](#projects-overview)
- [Installation](#installation)
- [Projects](#projects)
- [Usage Examples](#usage-examples)
- [API References](#api-references)

##  Projects Overview

| Project | API | Purpose | Status |
|---------|-----|---------|--------|
| **Plants** 🌿 | Perenual API | Fetch plant species information and care details | ✅ Active |
| **Pokemon** ⚡ | PokéAPI | Retrieve Pokémon stats, abilities, and artwork | ✅ Active |
| **Products** 🛍️ | Fake Store API | Browse e-commerce products with ratings | ✅ Active |
| **Weather** 🌦️ | Weather.com API | Get weather forecasts by geolocation | ✅ Active |

---

##  Installation

### Prerequisites
- Python 3.7+
- `requests` library

### Setup

```bash
# Clone the repository
git clone https://github.com/sanyagusain19/AI-ML-Bootcamp.git
cd AI-ML-Bootcamp/API

# Install dependencies
pip install requests
```

---

##  Projects

### 1. **Plants** 🌿 (`plants.py`)

Interact with the Perenual API to fetch plant species information and detailed plant care instructions.

#### Key Functions:
- **`fetch_plants(query="rose", page=1)`** - Search for plants by name with pagination
  - Returns: Plant list with common name, scientific name, watering needs, sunlight requirements, cycle, and family
  
- **`fetch_plant_detail(plant_id)`** - Get detailed information about a specific plant
  - Returns: Complete plant details including care instructions

#### Example Usage:
```python
from plants import fetch_plants, fetch_plant_detail

# Search for roses
result = fetch_plants(query="rose", page=1)
if result['success']:
    for plant in result['plants']:
        print(f"🌿 {plant['common_name']} ({plant['scientific_name']})")
        print(f"   Watering: {plant['watering']}")
        print(f"   Sunlight: {plant['sunlight']}")

# Get details for a specific plant
details = fetch_plant_detail(1)
```

#### API Details:
- **Base URL**: `https://perenual.com/api/v2/`
- **Authentication**: API Key required
- **Rate Limits**: Check Perenual documentation

---

### 2. **Pokemon** ⚡ (`pokemon.py`)

Fetch Pokémon data including stats, abilities, types, and official artwork.

#### Key Functions:
- **`fetch_pokemon(name)`** - Get Pokémon information by name or ID
  - Returns: Name, ID, image, types, abilities, and base stats (HP, Attack, Defense, etc.)

#### Example Usage:
```python
from pokemon import fetch_pokemon

# Get Pikachu data
pikachu = fetch_pokemon("pikachu")
if pikachu:
    print(f"⚡ {pikachu['name'].upper()}")
    print(f"   ID: {pikachu['id']}")
    print(f"   Types: {', '.join(pikachu['types'])}")
    print(f"   Abilities: {', '.join(pikachu['abilities'])}")
    print(f"   HP: {pikachu['stats']['hp']}")
    print(f"   Attack: {pikachu['stats']['attack']}")
```

#### API Details:
- **Base URL**: `https://pokeapi.co/api/v2/`
- **Authentication**: No API key required
- **Rate Limits**: 100 requests per IP per minute

---

### 3. **Products**  (`product.py`)

Browse and fetch e-commerce products with ratings and reviews from the Fake Store API.

#### Key Functions:
- **`fetch_products()`** - Get all available products
  - Returns: Product list with ID, title, price, category, image, rating, and description

#### Example Usage:
```python
from product import fetch_products

# Get all products
products = fetch_products()
for product in products:
    print(f"🛍️  {product['title']}")
    print(f"   Price: ${product['price']}")
    print(f"   Category: {product['category']}")
    print(f"   Rating: {product['rating']} ⭐ ({product['count']} reviews)")
```

#### API Details:
- **Base URL**: `https://fakestoreapi.com/`
- **Authentication**: No API key required
- **Rate Limits**: No strict limits (test/fake API)

---

### 4. **Weather** 🌦️ (`weather.py`)

Get weather forecasts for any location using latitude and longitude coordinates.

#### Key Functions:
- **`fetch_weather(lat=30.13, lon=77.28)`** - Get weather forecast
  - Parameters: Latitude and Longitude (defaults to Delhi, India)
  - Returns: 7-day weather forecast in JSON format

#### Example Usage:
```python
from weather import fetch_weather

# Get weather for Delhi, India (default)
weather_data = fetch_weather()

# Get weather for a custom location
# New York: lat=40.7128, lon=-74.0060
weather_ny = fetch_weather(lat=40.7128, lon=-74.0060)

if weather_data:
    print("🌦️  Weather Forecast:")
    print(weather_data)
```

#### API Details:
- **Base URL**: `https://api.weather.com/v3/wx/forecast/daily/7day`
- **Authentication**: API Key required
- **Units**: Metric (Celsius)
- **Language**: English-India

---

##  Usage Examples

### Complete Example: Multi-API Integration

```python
from plants import fetch_plants
from pokemon import fetch_pokemon
from product import fetch_products
from weather import fetch_weather

# 1. Check weather
print("=== Weather ===")
weather = fetch_weather(lat=40.7128, lon=-74.0060)
print(f"Weather data retrieved: {weather is not None}")

# 2. Get Pokémon info
print("\n=== Pokémon ===")
pokemon = fetch_pokemon("charizard")
if pokemon:
    print(f"{pokemon['name'].title()} - Types: {pokemon['types']}")

# 3. Browse products
print("\n=== Products ===")
products = fetch_products()
print(f"Total products: {len(products)}")
top_rated = max(products, key=lambda p: p['rating'])
print(f"Top rated: {top_rated['title']} ({top_rated['rating']}⭐)")

# 4. Search plants
print("\n=== Plants ===")
plants = fetch_plants(query="orchid")
if plants['success']:
    print(f"Found {plants['count']} orchids")
```

---

## 🔗 API References

| API | Documentation | Auth | Free Tier |
|-----|---------------|------|-----------|
| Perenual | [perenual.com](https://perenual.com/api) | API Key | ✅ Yes |
| PokéAPI | [pokeapi.co](https://pokeapi.co/) | None | ✅ Yes |
| Fake Store | [fakestoreapi.com](https://fakestoreapi.com/) | None | ✅ Yes |
| Weather.com | [weather.com/api](https://www.weather.com/api/) | API Key | ❌ No |

---

## ⚙️ Configuration

### Setting API Keys

Some projects require API keys. Create a `.env` file (if using python-dotenv):

```env
PERENUAL_API_KEY=sk-your-key-here
WEATHER_API_KEY=your-weather-api-key
```

Or directly update the constants in each file.

---

## 🐛 Error Handling

All functions include try-catch blocks and return status indicators:

```python
result = fetch_plants()
if result['success']:
    # Process data
    pass
else:
    # Handle error
    print(f"Error: {result['error']}")
```

---

##  Tips & Best Practices

- **Rate Limiting**: Respect API rate limits; add delays between requests if needed
- **Error Handling**: Always check the `success` flag before processing data
- **Caching**: Consider caching responses to reduce API calls
- **User Agents**: Some APIs require custom headers (included where needed)
- **Keys**: Never commit API keys to version control; use environment variables

---

##  License

This project is part of the AI-ML Bootcamp educational initiative.

---

##  Contributing

Feel free to add more API integrations! Follow the established pattern:

1. Create a new `.py` file with a descriptive name
2. Include error handling and status returns
3. Document functions with clear docstrings
4. Update this README

---



##  Support

For issues or questions:
- Check API documentation
- Review error messages in the console
- Test with curl or Postman first
- Open an issue on GitHub

