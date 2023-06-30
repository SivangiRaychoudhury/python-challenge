#import os module and csv module that allow us to create the file paths and read the csv files 
import os
import csv

#set the path for the .csv file
csvpath = os.path.join('/Users/soma/Desktop/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv')

#open and read the csv file using csv module
with open(csvpath) as csvfile:

    #csvreader specifies the delimiter and variable that holds contents in csvfile
    csvreader = csv.reader(csvfile, delimiter = ',') 

    #Read the header row first
    csv_header = next(csvreader)
    #print(csv_header)

    #Reads the first row excluding the header
    Poll_data = [next(csvreader)]
    
    #Initialising the variables
    Votes1=0
    Votes2=0
    Votes3=0
    Winner=0

    for row in csvreader:
     Poll_data.append(row)
    #total number of votes cast 
     Total_votes = len(Poll_data)
    

    for i in range(Total_votes):
    #print(row[2])   
     if str(Poll_data[i][2]) == "Charles Casper Stockham":
      Votes1 = Votes1+1
     elif str(Poll_data[i][2]) == "Diana DeGette":
      Votes2 = Votes2+1
     elif str(Poll_data[i][2]) == "Raymon Anthony Doane":
      Votes3 = Votes3+1
      

Max_votes=max(Votes1,Votes2,Votes3)
if Max_votes==Votes1:
 Winner = "Charles Casper Stockham"
elif Max_votes==Votes2:
 Winner = "Diana DeGette"
elif Max_votes==Votes3:
 Winner = "Raymon Anthony Doane"      
    
    



#List of candidates who received votes

#Percentage of votes each candidate won

#Total number of votes each candidate won

#Winner of the election based on popular votes




output = f'''
Election Results
------------------------
Total Votes: {Total_votes}
------------------------- 
Charles Casper Stockham: {100*Votes1/Total_votes: .3f}% ({Votes1})
Diana DeGette: {100*Votes2/Total_votes: .3f}% ({Votes2})
Raymon Anthony Doane: {100*Votes3/Total_votes: .3f}% ({Votes3})
-------------------------
Winner: {Winner}
------------------------
'''


print(output)
csvpath = os.path.join('/Users/soma/Desktop/Bootcamp/python-challenge/PyPoll/Analysis/PyPoll_Results.txt')
with open(csvpath,'w') as textfile:
 textfile.write(output)









#output:
#Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------