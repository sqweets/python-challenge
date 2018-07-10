# PyPoll application

# Last row incomplete
# data: 19129737, Queen, no candidate

import csv
import os

# Path to input file
pybank_csv = os.path.join("..", "..", "election_data.csv")

with open(pybank_csv, newline="") as csvfile:
    cin = csv.reader(csvfile, delimiter=",")
    next(cin) # Skip header

    # Initialization
    votes = 0
    candidates = {}

    # Calculations
    for row in cin:
        # Compute total votes
        votes += 1

        # Find candidates
        if (votes >= 2):
            if row[2] not in candidates:
                # Add new candidate
                candidate.append(row[2])
                candidate.append(1)
                candidates.append(row[2])
        else:
            # First candidate
            candidates.append(row[2])


    

    # Compute Average Change (and round to 2 decimals)
#    average_change = sum_of_monthly_change / (months - 1)
#    average_change = float("{0:.2f}".format(average_change))

    # Print Report

    # Print to text file
#    textfile = open("financial_analysis.txt", "w") 
 
#    textfile.write("Financial Analysis\n") 
 
#    textfile.close() 


