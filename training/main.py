import math
import time
import random

warehouse_items = [
    {"name": "Tile 60x60", "price": 6.50},
    {"name": "Tile 120x60", "price": 13.80},
    {"name": "wallpaper", "price": 10.00}
]

warehouse_sold_item = []



for i in range(1, 11):
    random_item = random.choice(warehouse_items)
    random_name = random_item["name"]


    print(f"Customer bought: {random_item['name']} for ${random_item['price']}")

    found = False
    for sold_item in warehouse_sold_item:
        if sold_item["name"] == random_name:
            sold_item["count"] += 1
            found = True
            break

    if not found:
        warehouse_sold_item.append({"name": random_name, "count": 1})

for items in warehouse_sold_item:
    print(items)
