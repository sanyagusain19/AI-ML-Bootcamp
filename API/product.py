import requests

def fetch_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    data = response.json()

    products = []

    for item in data:
        product = {
            "id": item["id"],
            "title": item["title"],
            "price": item["price"],
            "category": item["category"],
            "image": item["image"],
            "rating": item["rating"]["rate"],
            "count": item["rating"]["count"],
            "description": item["description"]
        }
        products.append(product)

    return products
    
