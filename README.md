# Python Challenge: PyBank & PyPoll

## Overview

This repository contains two Python projects from the Module 3 Challenge of a Data Analytics course. The tasks are designed to apply Python programming skills to solve real-world problems: analyzing financial data and processing election results.

### PyBank
In the PyBank challenge, the objective is to analyze the financial records of a company. The provided dataset contains monthly profit and loss records, and the task is to generate key financial metrics such as:
- Total number of months
- Net total amount of profit/losses
- Average change in profit/losses
- Greatest increase and decrease in profits

### PyPoll
In the PyPoll challenge, the goal is to analyze voting data from a small rural town's election. The dataset contains voter IDs, counties, and candidates. The task is to calculate:
- The total number of votes
- The percentage and total number of votes each candidate received
- The winner of the election based on the popular vote

Both scripts output the results to the terminal and save the analysis to a text file for each respective challenge.

## Project Structure

 python-challenge/ ├── PyBank/ │ ├── Resources/ │ │ └── budget_data.csv │ ├── analysis/ │ │ └── pybank.txt │ ├── main.py ├── PyPoll/ │ ├── Resources/ │ │ └── election_data.csv │ ├── analysis/ │ │ └── pypoll.txt │ ├── main.py └── README.md

 
- `main.py` for each challenge contains the script for performing the analysis.
- The `Resources` folders contain the datasets required for each task.
- The `analysis` folders contain the output text files with the results.

## Requirements

- Python 3.x
- Standard Python libraries (`os`, `csv`, `sys`, `statistics`, `collections`)

## How to Run

1. Clone the repository:
    ```bash
git clone https://github.com/yourusername/python-challenge.git

2. Navigate to the PyBank or PyPoll directory:
    ```bash
cd python-challenge/PyBank  # or cd python-challenge/PyPoll

3. Run the main.py script:
    ```bash
python main.py

4. The results will be printed to the terminal and saved in the analysis folder as a .txt file (pybank.txt or pypoll.txt).

## Example Output

### PyBank

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

### PyPoll

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------

## Notes

The CSV files (budget_data.csv and election_data.csv) should be placed in the Resources folder for each challenge.
Ensure that Python is installed and the working directory is correct before running the scripts.