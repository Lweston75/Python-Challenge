import os
# Import module for reading CSV files
import csv

#Append file directory and make a complete file path
filepath = os.path.join('PyBank','Resources','budget_data.csv')

#Initialize variables
Month_Count = 0
Total_PL = 0
PreValue = 0
Average = 0
Highest_Profit = 0
Lowest_Loss = 0
#Open and read CSV file
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
    
     for row in csvreader:
         month = row[0]
         Amount = row[1]
         Amount2 = int(Amount)
         Average =  Amount2 - PreValue
         #Greatest increase
         if Highest_Profit < Average:
            Highest_Profit = Average
            Highest_Profit_Month = month
         #Greatest decrease
         if Lowest_Loss > Average:
            Lowest_Loss = Average
            Lowest_Loss_Month = month

         PreValue = Amount2  
         # Total months
         Month_Count = Month_Count + 1
         # Total PL
         Total_PL += int(Amount) 

## Display Results ##   
  # Store the file path associated with the file (note the backslash may be OS specific)
file = 'input.txt'

# save as text
with open(file, 'w') as text:

    print(text)
    formatTxt = (

        'Financial Analysis\n'
        f'----------------------------\n'  
        #Total number of months 
        f'Total Months : {Month_Count}\n'
        #Total amount of "Profit/Losses"
        f'Total: $ {Total_PL}\n'
        # Average Change in "profit/Loss"
        f'Average Change: $ {Average}\n'
        # Greatest Increase in profit
        f'Greatest Increase in Profits: {Highest_Profit_Month} : ($ {Highest_Profit}\n'
        # Greatest Decrease in profit
        f'Greatest Decrease in Profits: {Lowest_Loss_Month} : ($ {Lowest_Loss})' 
    )
       text.write(formatTxt)
