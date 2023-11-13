## financial data analysis ##

# import modules before calling in the dataset
import os
import csv

# open the csv 
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# lists to store data
date = []
profit_loss = []
month = []
total = 0

#
with open(budget_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        
        date.append(row[0])

        profit_loss.append(row[1])

        #split dates into month and day
        split_date = row[0].split("-")
        month.append(split_date[0])

        for i in range(1, len(profit_loss)):
            
            #net total of profits/losses
            total = total + int(profit_loss[i])

            #average change in profit/losses over the entire period
            
            #greatest increase in profits (date and amount)
            max_profit = max(profit_loss[i])

            #greatest decrease in profits (date and amount)
            min_profit = min(profit_loss[i])


print(len(month) - 1)
print(total)
print(max_profit)
print(min_profit)