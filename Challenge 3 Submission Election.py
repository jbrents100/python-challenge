# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:28:07 2023

@author: jesse.brents
"""

import csv
import os

# Started by defining the file path uploaded a folder on my desktop that i named resources and put the data file inside, same for the analysis folder, created empty txt file and named it election_results
file_path = os.path.join("PyBank/Resources2/election_data.csv")

# named cariables and initialize the variables with a zero value
total_votes = 0
candidate_votes = {}

# Made sure that'analysis' directory exists even though I uploaded the folder with the empty txt file
analysis_dir = 'analysis'
if not os.path.exists(analysis_dir):
    os.makedirs(analysis_dir)

# used the with open function to read the CSV file
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Told the csv to skip the header row and continue on to the data
    next(csv_reader)
    
    for row in csv_reader:
        # Incremented total_votes
        total_votes += 1
        
        # Extracted the candidate names to fulfill the loop data requirement in step 3
        candidate_name = row[2]
        
        # Updated candidate vote counts using if/else
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Determined the winner of the election by using a max formula
winner = max(candidate_votes, key=candidate_votes.get)

# Printed the results to the terminal in the same order as the example
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Exported the same results to a text file on the analysis directory i setup earlier in the program and had created the folder and empty txt file as a precaution, lastly checked all values in the example to ensure they matched what populated in the terminal and in the txt file
output_path = os.path.join("PyBank/analysis2/election_results.txt")
with open(output_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
