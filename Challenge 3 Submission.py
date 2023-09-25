# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:12:40 2023

@author: jesse.brents
"""

import csv  # created a folder for resources and analysis with csv and txt files for the file paths to work

# Define the file path for my data where the folder is resources did the same for the ouput so that I created a folder named analysis and the output text file named financial_analysis
file_path = "PyBank/Resources/budget_data.csv"

# Establish the variable names and values
total_months = 0
net_total = 0
changes = []
greatest_increase = 0  # zero is so that to correctly find the greatest increase, initialize with a very small number.
greatest_decrease = 0  #again zero is so that to correctly find the greatest decrease, initialize with a very large number.
greatest_increase_date = ""  # For storing the date of greatest increase
greatest_decrease_date = ""  # For storing the date of greatest decrease
previous_profit_loss = None  # For storing the previous month's profit/loss value

# tell the program to read the CSV file
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # added Skip header row
    next(csv_reader)
    
    # Iterated through the data set and calculate values from the Date and Profit/Loss Columns
    for row in csv_reader:
        # Extracted date and profit/loss
        date = row[0]
        profit_loss = int(row[1])
        
        # Incremented total_months and Update net_total
        total_months += 1
        net_total += profit_loss
        
        # Calculated change in profit/loss and Update greatest_increase and greatest_decrease
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            elif change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date
        
        # Updated previous_profit_loss for the next iteration
        previous_profit_loss = profit_loss

# Calculated average change
average_change = sum(changes) / len(changes) if changes else 0  # Avoid division by zero

# Printed results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Exported results to a text file
output_file_path = "PyBank/analysis/financial_analysis.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
