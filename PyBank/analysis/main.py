## financial data analysis ##

# import module before calling in a dataset
import os
import csv

# open the csv 
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

