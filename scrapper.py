from bs4 import BeautifulSoup
import pandas as pd
import requests

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(start_url, verify = False)
headers = ["Name", "Distance", "Mass", "Radius"]

def scrape():
    star_data = []
    soup = BeautifulSoup(page.text, "html.parser")
    table_tag = soup.find('table')
    tr_tags = table_tag.find_all('tr')
    for tr in tr_tags:
        td_tags = tr.find_all('td')
        data = [i.text.strip() for i in td_tags]
        star_data.append(data)

    name, distance, mass, radius = [], [], [], []

    for i in range(1, len(star_data)):
        name.append((star_data[i][1]))
        distance.append(star_data[i][3])
        mass.append((star_data[i][5]))
        radius.append(star_data[i][6])

    final_list = list(zip(name, distance, mass, radius))

    df = pd.DataFrame(final_list, columns = headers)
    df.to_csv("Bright-Stars.csv")

scrape()