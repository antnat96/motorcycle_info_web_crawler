import requests
from bs4 import BeautifulSoup
import xlsxwriter
import psycopg2
import json

#### STRUCTURE ####
# go to home page
# set full info json object
# go to each make page
    # go to each model page
        # grab the information
        # add it to the full info json object
# turn info list into excel spreadsheet or postgresql db

# go to home page, create soup, get makes
BASE_URL = "https://www.motorcyclespecs.co.za/"
home_page = requests.get(BASE_URL)
home_soup = BeautifulSoup(home_page.content, "html.parser")
makes = home_soup.select("div[class=subMenu] > a")
# set big info list
full_info = {}

# go to each make page
j = 0
for x in makes:
    # Skip the first several links, they're not important
    if j > 7:
        # to only look at a certain make, uncomment and change "Honda" to the make
        # if "Honda" in x.text:
            # Get the link to the page with a list of the models for that make
            make_URL = BASE_URL + x.get("href").split("../../")[1] 
            # Request the page
            make_page = requests.get(make_URL) 
            # Get the soup
            make_soup = BeautifulSoup(make_page.content, "html.parser")
            # Get all the links to each individual model 
            models = make_soup.select("td > a")

            # go to each model page
            for x in models:
                print("Second")
                # Only if it's a model
                if "../model/" in x.get("href"):
                    
                    # grab the information
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

def go_to_next(make_URL):
    # follow link
    # get info
    # if there is a link below it, follow that

def add_info_to_db(info_array):
    conn = psycopg2.connect(host="localhost", port = 5432, database="postgres", user="postgres", password="postgres_password")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM vendors""")
    query_results = cur.fetchall()
    print(query_results)
    cur.close()
    conn.close()

def create_workbook(info):
    # Set up the workbook
    workbook = xlsxwriter.Workbook("motorcycle_info.xlsx")
    worksheet = workbook.add_worksheet("Sheet_1")
    row = 0
    col = 0