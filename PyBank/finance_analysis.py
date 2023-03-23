import os
import sys
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

total_months = 0
profit = 0
net_change = 0
max_profit = -sys.maxsize - 1
max_date = ""
min_profit = sys.maxsize
min_date = ""

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    previous_profit = 0

    next(csvreader)
    for row in csvreader:
        total_months += 1
        profit += int(row[1])
        if previous_profit != 0:
            net_change += (int(row[1]) - previous_profit)
        if max_profit <= (int(row[1]) - previous_profit):
            max_profit = int(row[1]) - previous_profit
            max_date = row[0]
        if min_profit >= (int(row[1]) - previous_profit):
            min_profit =  int(row[1]) - previous_profit
            min_date = row[0]
        previous_profit = int(row[1])


avg_net_change = round(net_change / (total_months - 1), 2)
print("Finacial Analysis"
    + "\nTotal Months: " + str(total_months) 
    + "\nTotal: $" + str(profit) 
    + "\nAverage Change: $" + str(avg_net_change) 
    + "\nGreatest Increase in Profits: " + str(max_date) + " ($" + str(max_profit) + ")" 
    + "\nGreatest Decrease in Profits: " + str(min_date) + " ($" + str(min_profit) + ")")

with open("budget_analysis.txt", 'w') as file:
    file.write("Finacial Analysis")
    file.write("\nTotal Months: " + str(total_months))
    file.write("\nTotal: $" + str(profit))
    file.write("\nAverage Change: $" + str(avg_net_change))
    file.write("\nGreatest Increase in Profits: " + str(max_date) + " ($" + str(max_profit) + ")")
    file.write("\nGreatest Decrease in Profits: " + str(min_date) + " ($" + str(min_profit) + ")")