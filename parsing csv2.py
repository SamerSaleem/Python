import csv

with open("parsing.csv") as data:
    csv_list = csv.reader(data)
    for row in csv_list:
        device = row[0]
        location = row [1]
        ip = [2]
        print(f"{device} is in {location.rstrip()} and has ip {ip}.")
        