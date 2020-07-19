import requests
from bs4 import BeautifulSoup
import xlsxwriter
import psycopg2

# Set up the workbook
# workbook = xlsxwriter.Workbook("makes.xlsx")
# worksheet = workbook.add_worksheet("Makes")
row = 0
col = 0

# Makes
BASE_URL = "https://www.motorcyclespecs.co.za/"
makes_page = requests.get(BASE_URL)
makes_soup = BeautifulSoup(makes_page.content, "html.parser")
makes_menu_items = makes_soup.select("div[class=subMenu] > a")

j = 0
# Loop through each make link
for x in makes_menu_items:
    print("First")
    # Looping through the bottom menu first two items 
    if j > 7:
        if "Honda" in x.text:
            # Get the link to the page with a list of the models for that make
            make_URL = BASE_URL + x.get("href").split("../../")[1] 
            # Request the page
            make_page = requests.get(make_URL) 
            make_soup = BeautifulSoup(make_page.content, "html.parser")
            # Get all the links to each individual model 
            model_menu_items = make_soup.select("td > a")
            for x in model_menu_items:
                print("Second")
                # Only if it's a model
                if "../model/" in x.get("href"):
                    # Info
                    info_URL = BASE_URL + x.get("href").split("../")[1]
                    info_page = requests.get(info_URL)
                    info_soup = BeautifulSoup(info_page.content, "html.parser")
                    info_columns = info_soup.find_all("td", {"width":"30%"})
                    info_columns_text = []
                    info_rows = info_soup.find_all("td", {"width":"70%"})
                    info_rows_text = []
                    for x in info_columns:
                        print("Third")
                        info_columns_text.append(x.text.replace("\n",""))
                        print(x.text.replace("\n",""))
                    for x in info_rows:
                        info_rows_text.append(x.text.replace("\n",""))
                        print(x.text.replace("\n",""))
    j += 1

def add_info_to_db(info_array):
    conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="postgres", password="postgres_password")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM vendors""")
    query_results = cur.fetchall()
    print(query_results)
    cur.close()
    conn.close()