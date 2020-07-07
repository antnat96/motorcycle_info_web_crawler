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
i = j = 0

for x in makes_menu_items:
    if i > 7:
        makes_list.append(x.string) # Makes to be added to the workbook
    i += 1
    
for x in makes_menu_items:
    if j > 7:    
        # Models
        models_URL = makes_URL + x.get("href").split("../../")[1]
        models_page = requests.get(models_URL)
        models_soup = BeautifulSoup(models_page.content, "html.parser")
        models_menu_items = models_soup.select("div[class=subMenu] > a")
        models_list = []
        models_links = []
        for x in models_menu_items:
            models_list.append(x.string) # Models to be added to the workbook
        for x in models_menu_items:
            # Info
            info_URL = models_URL + x.get("href").split("../../")[1]
            info_page = requests.get(info_URL)
            info_soup = BeautifulSoup(info_page.content, "html.parser")
            info_menu_items = info_soup.select("div[class=subMenu] > a")
            info_list = []
            info_links = []
            for x in info_menu_items:
                info_list.append(x.string) # Info to be added to the workbook
            for x in info_menu_items:
                info_links.append(info_URL + x.get("href").split("../../")[1])
    j += 1