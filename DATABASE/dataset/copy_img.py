import csv
import os 
import shutil

file = open("label_nosenet.csv")
csvreader = csv.reader(file)

image_path = "DataSet/"
dest = "images/"

for rows in csvreader:
    if rows[0] == "nose":
        file_name = image_path + rows[3]
        if(os.path.isfile(file_name)):
            shutil.move(file_name,dest)