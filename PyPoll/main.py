import os
import csv
import sys

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# I used a full path (below) to get this code to work on my computer. 
# csvpath = "C://Users//matth//OneDrive//Desktop//Data Analytics Class//Module 3 - Python//Challenge//PyPoll//Resources//election_data.csv"

# Redirect output to a text file named "pybank.txt"
output_file = "pypoll.txt"
output_path = os.path.join(os.getcwd(), output_file)

# Open the output file for writing
with open(output_path, "w") as f_out:

    # Open the CSV file for reading
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip header
        headers = next(csvreader) 

        # Initialize total vote variable
        total_votes = len(list(csvfile))

        # Total vote results
        print ('Election Results')
        print("")
        print('----------------------------')
        print("")
        print('Total Votes: ' + str(total_votes))
        print("")
        print('----------------------------')
        print("")

        print ('Election Results', file=f_out)
        print("", file=f_out)
        print('----------------------------', file=f_out)
        print("", file=f_out)
        print('Total Votes: ' + str(total_votes), file=f_out)
        print("", file=f_out)
        print('----------------------------', file=f_out)
        print("", file=f_out)

        #Create candidate list
        from collections import Counter
        with open(csvpath) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            headers = next(csvreader) 
            candidate_list = []

            for row in csvreader:
                candidate_list.append(row[2])

        # Initialize variable for candidates
        candidates = Counter(candidate_list)

        # Calculate votes and percentage by candidate
        stockham_votes = (candidates['Charles Casper Stockham'])
        stockham_percentage = round(int(candidates['Charles Casper Stockham']) / int(total_votes) * 100, 3)
        degette_votes = (candidates['Diana DeGette'])
        degette_percentage = round(int(candidates['Diana DeGette']) / int(total_votes)  * 100, 3)
        doane_votes = (candidates['Raymon Anthony Doane'])
        doane_percentage = round(int(candidates['Raymon Anthony Doane']) / int(total_votes)  * 100, 3)

        # Calculate winner
        winner = max(stockham_votes, degette_votes, doane_votes)
        if winner == stockham_votes:
            winner_name = "Charles Casper Stockham"
        elif winner == degette_votes:
            winner_name = "Diana DeGette"
        else:
            winner_name = "Raymon Anthony Doane"

        # Print results
        print(f"Charles Casper Stockham: {stockham_percentage}% ({stockham_votes})")
        print("")
        print(f"Diana DeGette: {degette_percentage}% ({degette_votes})")
        print("")
        print(f"Raymon Anthony Doane: {doane_percentage}% ({doane_votes})")
        print("")
        print('----------------------------')
        print("")
        print(f"Winner: {winner_name}")
        print("")
        print('----------------------------')

        print(f"Charles Casper Stockham: {stockham_percentage}% ({stockham_votes})", file=f_out)
        print("", file=f_out)
        print(f"Diana DeGette: {degette_percentage}% ({degette_votes})", file=f_out)
        print("", file=f_out)
        print(f"Raymon Anthony Doane: {doane_percentage}% ({doane_votes})", file=f_out)
        print("", file=f_out)
        print('----------------------------', file=f_out)
        print("", file=f_out)
        print(f"Winner: {winner_name}", file=f_out)
        print("", file=f_out)
        print('----------------------------', file=f_out)
