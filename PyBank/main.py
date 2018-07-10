# PyBank application

import csv
import os

# Path to input file
pybank_csv = os.path.join("..", "..", "budget_data.csv")

with open(pybank_csv, newline="") as csvfile:
    cin = csv.reader(csvfile, delimiter=",")
    next(cin) # Skip header

    # Initialization
    months = 0
    sum_of_revenue = 0
    average_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    previous_month = 0
    sum_of_monthly_change = 0
    gi_date = ""
    gd_date = ""

    # Calculations
    for row in cin:
        # Compute total months
        months += 1

        # Sum of Revenue
        sum_of_revenue = sum_of_revenue + int(row[1])

        # Average change per month
        # Start calculations on second month
        if (months >= 2):
            change = int(row[1]) - previous_month
            previous_month = int(row[1])
        else:
            # First month
            change = 0
            previous_month = int(row[1])

        # Add change to running sum
        sum_of_monthly_change = sum_of_monthly_change + change

        # Save greatest increase
        if (change > greatest_increase):
            greatest_increase = change
            gi_date = row[0]
        elif (change < greatest_decrease):
            greatest_decrease = change
            gd_date = row[0]

    # Compute Average Change (and round to 2 decimals)
    average_change = sum_of_monthly_change / (months - 1)
    average_change = float("{0:.2f}".format(average_change))

    # Print Report
    print("\nFinancial Analysis")
    print("---------------------------")
    print("Total Months: " + str(months))
    print("Total: $" + str(sum_of_revenue))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: " + gi_date + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + gd_date + " ($" + str(greatest_decrease) + ")")

    # Print to text file
    textfile = open("financial_analysis.txt", "w") 
 
    textfile.write("Financial Analysis\n") 
    textfile.write("---------------------------\n") 
    textfile.write("Total Months: " + str(months) + "\n") 
    textfile.write("Total: $" + str(sum_of_revenue) + "\n") 
    textfile.write("Average Change: $" + str(average_change) + "\n") 
    textfile.write("Greatest Increase in Profits: " + gi_date + " ($" + str(greatest_increase) + ")" + "\n") 
    textfile.write("Greatest Decrease in Profits: " + gd_date + " ($" + str(greatest_decrease) + ")" + "\n") 
 
    textfile.close() 


