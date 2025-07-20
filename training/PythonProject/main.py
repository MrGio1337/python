import os
import random

txt_data = "This is a test file"
item_storage_data = 65

output_file = "output.txt"

with open(output_file, "w", encoding="utf-8") as file:
    generatedRandomSum = random.randint(1, 5)
    generatedCheckNumID = random.randint(10000, 9999999)

    if item_storage_data <= 0:
        print("Out of stock.")

    item_storage_data = item_storage_data - generatedRandomSum

    check_data = [
        "********************************************",
        f"       Check ID: {generatedCheckNumID}     ",
        "********************************************",
        "- შეკიდული ჭერი | PH257 | ",
        f"- რაოდენობა: {generatedRandomSum} ცალი | კვადრატი: {generatedRandomSum * 1500} | მეტრი: 6+",
        f"- რაოდენობა საწყობში: {item_storage_data - generatedRandomSum} ცალი | კვადრატი: {item_storage_data * 1500}"
    ]

    for checkData in check_data:
        file.write(checkData + "\n")

    print(f"{output_file} was created.")