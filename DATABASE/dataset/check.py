import csv
import os

file = open("nosenet.csv")
csvreader = csv.reader(file)

img_folder = "images/"
img_cout = 0

for row in csvreader:
    img_path = img_folder + row[3]
    if(os.path.isfile(img_path)):
        img_cout += 1
    
print("image count {}".format(img_cout))