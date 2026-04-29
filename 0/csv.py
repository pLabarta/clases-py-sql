import csv

with open("data.csv", newline='', encoding="utf-8") as file:
    print("Hello world!")
    reader = csv.reader(file)
    for row in reader:
        print(row)