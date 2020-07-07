import requests
from bs4 import BeautifulSoup
import xlsxwriter

# Set up the workbook
# workbook = xlsxwriter.Workbook("makes.xlsx")
# worksheet = workbook.add_worksheet("Makes")
row = 0
col = 0

# Makes
makes_URL = "https://www.motorcyclespecs.co.za/"
makes_page = requests.get(makes_URL)
makes_soup = BeautifulSoup(makes_page.content, "html.parser")
makes_menu_items = makes_soup.select("div[class=subMenu] > a")
makes_list = []
makes_links = []
i = 0
j = 0

for x in makes_menu_items:
    makes_list.append(x.string)
    print(makes_list[i])
    i = i + 1
for x in makes_menu_items:
    makes_links.append(makes_URL + x.get("href").split("../../")[1])
    print(makes_links[j])
    j = j + 1


# Models