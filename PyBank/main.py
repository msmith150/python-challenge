import os
import csv
import sys
from statistics import mean

# Define the path to your CSV file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# I used a full path (below) to get this code to work on my computer. 
# csvpath = "C://Users//matth//OneDrive//Desktop//Data Analytics Class//Module 3 - Python//Challenge//PyBank//Resources//budget_data.csv" 

# Redirect output to a text file named "pybank.txt"
output_file = "pybank.txt"
output_path = os.path.join(os.getcwd(), output_file)

# Open the output file for writing
with open(output_path, "w") as f_out:
    
    # Open the CSV file for reading
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip header
        headers = next(csvreader)

        # Create lists for date and profit/losses
        date = []
        profit_losses = []

        # Read data from CSV and populate lists
        for row in csvreader:
            date.append(row[0])
            profit_losses.append(int(row[1]))

        # Total number of months
        total_months = len(date)
        print('Financial Analysis')
        print('----------------------------')
        print(f'Total Months: {total_months}')
        print(f'Total: ${sum(profit_losses)}')

        print('Financial Analysis', file=f_out)
        print('----------------------------', file=f_out)
        print(f'Total Months: {total_months}', file=f_out)
        print(f'Total: ${sum(profit_losses)}', file=f_out)

        # Calculate changes in profit/losses
        changes = [profit_losses[i+1] - profit_losses[i] for i in range(len(profit_losses) - 1)]
        average_change = mean(changes)
        print(f'Average Change: ${round(average_change, 2)}')
        print(f'Average Change: ${round(average_change, 2)}', file=f_out)

        # Find greatest increase and decrease in profits
        max_increase = max(changes)
        max_increase_index = changes.index(max_increase) + 1
        max_increase_date = date[max_increase_index]
        print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')
        print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})', file=f_out)

        max_decrease = min(changes)
        max_decrease_index = changes.index(max_decrease) + 1
        max_decrease_date = date[max_decrease_index]
        print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')
        print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})', file=f_out)




