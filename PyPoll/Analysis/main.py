import os
import csv



# Set path for file
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

#Open and read CVS File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    header = next(csvreader)
    
    #variables
    Total_Votes = 0
    Khan_Votes = 0
    Li_Votes = 0
    Otooley_Votes = 0
    Correy_Votes = 0 
    Kahn_Per = 0.00
    Li_Per = 0.00
    Otooley_Per = 0.00
    Correy_Per = 0.00
    Winning_Votes = 0
    winner = ""
    for row in csvreader:
        Total_Votes = Total_Votes + 1
        #Khan Votes
        if(row[2] == 'Khan'): 
            Khan_Votes = Khan_Votes + 1
        #Li Votes
        elif (row[2] == 'Li'):
            Li_Votes = Li_Votes + 1
        #O'Tooley Votes
        elif (row[2] == "O'Tooley"): 
            Otooley_Votes = Otooley_Votes + 1
        #Correy Votes
        elif (row[2] == 'Correy'): 
            Correy_Votes = Correy_Votes + 1
# Khan %
Khan_Per = Khan_Votes / Total_Votes * 100
# Li %
Li_Per = Li_Votes / Total_Votes * 100
# O'Tooley %
Otooley_Per = Otooley_Votes / Total_Votes * 100
# Correy %
Correy_Per = Correy_Votes / Total_Votes * 100
# type out the winner
Winning_Votes = max(Khan_Votes, Li_Votes, Otooley_Votes, Correy_Votes)
if(Winning_Votes == Khan_Votes):
    winner = 'Khan' 
elif(Winning_Votes == Li_Votes):
    winner = 'Li'
elif(Winning_Votes == Otooley_Votes):
    winner = "O'Tooley"
elif(Winning_Votes == Correy_Votes):
    winner = 'Correy'


# Results
  
file = 'imput.txt'

# Save as Text
with open(file, 'w') as text:

   
    print(text)
    formatTxt = (
        f'Election Results\n'
        f'--------------------------------\n'
        #Total number of votes
        f'Total votes: {str(Total_Votes)}\n'
        f'--------------------------------\n'
        #Candidate data
        f'Khan: {str(Khan_Per)} % '
        f'({str(Khan_Votes)})\n'
        f'LI: {str(Li_Per)} % '
        f'({str(Li_Votes)})\n'
        f"O'Tooley: {str(Otooley_Per)} % "
        f'({str(Otooley_Votes)})\n'
        f'Correy: {str(Correy_Per)} % '
        f'({str(Correy_Votes)})\n'
        f'--------------------------------\n'
        #Select and Print Winner
        f'Winner: {str(winner)}\n'
        f'--------------------------------'
    )
    text.write(formatTxt)