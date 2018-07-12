# PyPoll application

# NOTE 1
# Last row incomplete in datafile
# data: 19129737, Queen, no candidate
# Deleted since invalid

# NOTE 2
# The code below works but its not very elegant mainly because of calculating the percent twice.
# Since this is a small dataset, etc. I left as is, however, the way think I would fix this is to
# change the dict to a dictionary of lists with the lists being [votes, percentage of votes].
# However, I don't know how to handle the for loop starting at line 30.  Suggestions welcome.

import csv
import os

# Path to input file
pypoll_csv = os.path.join("..", "..", "election_data.csv")

with open(pypoll_csv, newline="") as csvfile:
    cin = csv.reader(csvfile, delimiter=",")
    next(cin) # Skip header

    # Initialization
    votes = 0
    candidates = {}

    # Find the candidates
    for row in cin:
        # Compute total votes
        votes += 1

        # Add candidates and sum up votes
        if row[2] not in candidates:
            # Add new candidate
            candidates[row[2]] = 1
        else:
            # Increment votes
            candidates[row[2]] += 1

    winner = ''
    current_highest_votes = 0

    # Print to terminal
    print("\nElection Results")
    print("-------------------------")
    print("Total Votes: " + str(votes))
    print("-------------------------")
    for key, value in candidates.items():
        # Figure out the winner
        if (value > current_highest_votes):
            current_highest_votes = value
            winner = key

        # Print out each candidates data
        print(key + ": "+ str(float("{0:.2f}".format(100 * (value/votes)))) + "% (" + str(value) + ")")
    print("-------------------------")
    print("Winner: " + winner)
    print("-------------------------")

    # Print to text file
    textfile = open("voting_analysis.txt", "w") 
 
    textfile.write("Election Results\n") 
    textfile.write("-------------------------\n") 
    textfile.write("Total Votes: " + str(votes) + "\n") 
    textfile.write("-------------------------\n") 
    for key, value in candidates.items():
        # Print out each candidates data
        textfile.write(key + ": "+ str(float("{0:.2f}".format(100 * (value/votes)))) + "% (" + str(value) + ")\n")
    textfile.write("-------------------------\n")
    textfile.write("Winner: " + winner + "\n")
    textfile.write("-------------------------\n")
 
    textfile.close() 

    
