import requests
import random

def get_random_pizzas(quantity=2):
    """Returns a list of pizza names."""
    if quantity > 50:
        raise ValueError('Max quantity is 50')
    products = []
    payload = {
        "action": "process",
        "json": 1,
        "tagtype_0": "categories",
        "tag_contains_0": "contains",
        "tag_0": "pizzas",
        "page_size": 100
    }
    response = requests.get(
        'https://fr.openfoodfacts.org/cgi/search.pl',
        params=payload
    )
    if response.status_code == 200:
        products = response.json()['products']

    return random.sample([
        product['product_name'] for product in products
        if 'product_name' in product
    ], quantity)

if __name__ == "__main__":
    print(get_random_pizzas(5))