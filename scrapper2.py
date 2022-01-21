from bs4 import BeautifulSoup
import pandas as pd
import requests

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(start_url, verify = False)
headers = ["Name", "Distance", "Mass", "Radius"]

def scrape():
    dwarf_star_data = []
    soup = BeautifulSoup(page.text, "html.parser")
    table_tag = soup.find_all('table')
    tr_tags = table_tag[7].find_all('tr')
    for tr in tr_tags:
        td_tags = tr.find_all('td')
        data = [i.text.strip() for i in td_tags]
        dwarf_star_data.append(data)

    name, distance, mass, radius = [], [], [], []

    for i in range(1, len(dwarf_star_data)):
        name.append((dwarf_star_data[i][0]))
        distance.append(dwarf_star_data[i][5])
        mass.append((dwarf_star_data[i][7]))
        radius.append(dwarf_star_data[i][8])

    final_list = list(zip(name, distance, mass, radius))

    df = pd.DataFrame(final_list, columns = headers)
    df.to_csv("Dwarf Brown Stars.csv")

scrape()