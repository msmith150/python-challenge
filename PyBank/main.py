import os
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = "C://Users//matth//OneDrive//Desktop//Data Analytics Class//Module 3 - Python//Challenge//PyBank//Resources//budget_data.csv"

import csv

from statistics import mean

###################To output to file############ (https://stackoverflow.com/questions/25023233/how-to-save-python-screen-output-to-a-text-file)

import sys 

stdoutOrigin=sys.stdout 
sys.stdout = open("pybank.txt", "w")

##########################################################################################################################

with open(csvpath) as csvfile:

  csvreader = csv.reader(csvfile, delimiter=',')
  headers = next(csvreader) 

  date = [row[0] for row in csvreader]
  months = [row[0].split("-")[0] for row in csvreader]
  total_months = (len(months))
  print ('Financial Analysis')
  print('----------------------------')
  print('Total Months: ' + str(total_months))

  # The net total amount of "Profit/Losses" over the entire period

with open(csvpath) as csvfile:

  csvreader = csv.reader(csvfile, delimiter=',')
  headers = next(csvreader) 

  profit_losses_strings = [row[1] for row in csvreader]
  profit_losses = [int(num) for num in profit_losses_strings]
  net_total = sum(profit_losses)
  print(f"Total: ${net_total}")

# #The changes in "Profit/Losses" over the entire period, and then the average of those changes

  diff = [profit_losses[i+1]-profit_losses[i] for i in range(len(profit_losses)-1)] #https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list
  av_change = mean(diff)

print(f"Average Change: ${round(av_change)}")
# #The greatest increase in profits (date and amount) over the entire period
g_increase = max(diff)
max_date_index = (diff.index(max(diff)) + 1)
increase_date = date[max_date_index]    
print(f"Greatest Increase in Profits: {increase_date} ${g_increase}")

# #The greatest decrease in profits (date and amount) over the entire period
g_decrease = min(diff)
min_date_index = (diff.index(min(diff)) + 1)
decrease_date = date[min_date_index]
print(f"Greatest Decrease in Profits: {decrease_date} ${g_decrease}")

############To print############

sys.stdout.close()
sys.stdout=stdoutOrigin