import requests
from bs4 import BeautifulSoup
import lxml
import json

# url = "https://maytoni.ru/catalog/decorative/"
#
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)
# with open("pythonProject/Catalog/Decorative/index.html", "w") as file:
#     file.write(src)

# with open("pythonProject/Catalog/Decorative/index.html") as file:
#    src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
# all_product_hrefs = soup.find_all(class_="category-menu__link", )
#
# all_categories_dict = {}
# for item in all_product_hrefs:
#    item_text = item.text
#    item_href = "https://maytoni.ru" + item.get("href")
#
#    all_categories_dict[item_text] = item_href
# with open("pythonProject/Catalog/Decorative/all_categories_dict.json", "w") as file:
#    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
#    print(item_text, item_href)

with open("pythonProject/Catalog/Decorative/all_categories_dict.json") as file:
   all_categories = json.load(file)

for categories_name, categories_href in all_categories.items():

   rep = [" "]
   for item in rep:
      if item in categories_name:
         categories_name = categories_name.replace(item, "")
      print(categories_name)
#str1 = str1.replace('\t', '')
