import csv

dataset_1 = []
dataset_2 = []

with open("Bright-Stars.csv", "r") as f1:
    reader = csv.reader(f1)
    for i in reader:
        dataset_1.append(i)

with open("Dwarf-Brown-Stars.csv", "r") as f2:
    reader = csv.reader(f2)
    for j in reader:
        dataset_2.append(j)

header_1 = dataset_1[0]
header_2 = dataset_2[0]
star_data_1 = dataset_1[1:]
star_data_2 = dataset_2[1:]

headers = header_1 + header_2
star_data = []

for index, data in enumerate(star_data_1):
    star_data.append(star_data_1[index] + star_data_2[index])

with open("Dwarf-Brown-Stars-Units-Converted.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(star_data)