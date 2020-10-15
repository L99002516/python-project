import csv
your_list=[]
with open('dat.csv', newline='') as f:
    reader = csv.reader(f)
    your_list = list(reader)
    
