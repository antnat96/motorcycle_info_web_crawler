import requests
from bs4 import BeautifulSoup

URL = "https://www.motorcyclespecs.co.za/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

makes_menu = soup.select("div[class=subMenu] > a")

makes_list = []

for x in makes_menu:
    makes_list.append(x.string)

print(makes_list[0])