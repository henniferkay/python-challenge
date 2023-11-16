## financial data analysis ##

# import modules before calling in the dataset
import os
import csv

# open the csv 
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# create the variables of interest and set them to certain values to start from
number_of_months = 0
total = 0
previous_revenue = 0
change = 0

# create lists to hold the profits/losses and respective dates
profit_loss = []
dates = []

# read csv file
with open(budget_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #header row
    headers = next(csvreader)

    #first row
    first_row = next(csvreader)

    #start the number of months
    number_of_months += 1

    #start the total of profits/losses
    total += int(first_row[1])

    #starting profit/loss value
    previous_revenue = int(first_row[1])
    
    #start a loop that goes by row from the first row
    for row in csv.reader(csvfile):

        #total number of months
        number_of_months += 1

        #total profits/losses
        total += int(row[1])

        #keep the changes in profit/loss by row
        change = int(row[1]) - previous_revenue
        profit_loss.append(change)
        previous_revenue = int(row[1]) #reset

        #obtain the date of each row and store into the date list
        dates.append(row[0])

# calculate the average change in profits and losses
avg_change = sum(profit_loss)/len(profit_loss)

# greatest increase in profits (date and amount)
greatest_increase = max(profit_loss)
greatest_increase_index = profit_loss.index(greatest_increase)
greatest_increase_date = dates[greatest_increase_index]

# greatest decrease in profits (date and amount)
greatest_decrease = min(profit_loss)
greatest_decrease_index = profit_loss.index(greatest_decrease)
greatest_decrease_date = dates[greatest_decrease_index]

# print out the variables created from above to check if the code worked successfully
print(number_of_months)
print(total)
print(avg_change)
print(greatest_increase)
print(greatest_increase_date)
print(greatest_decrease)
print(greatest_decrease_date)

# generate output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {number_of_months}\n"
    f"Total: ${total:,}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:,})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:,})\n")

# print the output
print(output)

# export the results to text file
with open("output.txt", "w") as txt_file:
    txt_file.write(output)