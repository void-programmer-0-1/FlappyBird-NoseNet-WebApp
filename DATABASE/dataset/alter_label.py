import csv

with open('label_nosenet.csv', 'r') as inp, open('nosenet.csv', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[0] == "nose":
            writer.writerow(row)

