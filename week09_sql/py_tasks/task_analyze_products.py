
def analyze_products(products: list[dict]) -> dict:
    result = {
    "total_products": 0,
    "unique_categories": set(),
    "out_of_stock": [],
    "avg_price_by_category": {},
    "total_stock": 0,
}
    price_by_category = {}
    result['total_products'] = len(products)
    for product in products:
        result['unique_categories'].add(product['category'])
        if product['stock'] == 0:
            result['out_of_stock'].append(product['name'])
        category = product['category']
        if category not in price_by_category:
            price_by_category[category] = []
        price_by_category[category].append(product['price'])
        result['total_stock'] += product['stock']
    for category, prices in price_by_category.items():
        average = sum(prices) / len(prices)
        result['avg_price_by_category'][category] = round(average, 2)

    return result


if __name__ == '__main__':
    products = [
        {"name": "Laptop Pro 15", "category": "Electronics", "price": 1499.99, "stock": 25},
        {"name": "Wireless Mouse", "category": "Electronics", "price": 29.99, "stock": 150},
        {"name": "Coffee Maker", "category": "Home", "price": 89.50, "stock": 60},
        {"name": "Yoga Mat", "category": "Fitness", "price": 25.00, "stock": 200},
        {"name": "Running Shoes", "category": "Fitness", "price": 120.00, "stock": 100},
        {"name": "Wireless Charger", "category": "Electronics", "price": 35.00, "stock": 0},
    ]

    result = analyze_products(products)
    print(result["total_products"])           # 6
    print(result["unique_categories"])         # {'Electronics', 'Home', 'Fitness'}
    print(result["out_of_stock"])              # ['Wireless Charger']
    print(result["avg_price_by_category"])     # {'Electronics': 521.66, 'Home': 89.5, 'Fitness': 72.5}
    print(result["total_stock"])                # 535

    # Пустой список
    empty = analyze_products([])
    print(empty)
    # {'total_products': 0, 'unique_categories': set(), 'out_of_stock': [], 'avg_price_by_category': {}, 'total_stock': 0}