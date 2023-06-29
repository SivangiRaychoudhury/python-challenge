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
    Names = []
    Votes_per_Candidate = 0
    Percentage = 0

    for row in csvreader:
     Poll_data.append(row)
    #total number of votes cast 
     Total_votes = len(Poll_data)
    

    for i in range(Total_votes):
    #print(row[2])   
     if Poll_data[i-1][2] != Poll_data[i][2]:
      Names = Poll_data[i][2]
      print(Names) 
      i=Total_votes
        #elif str(row[2]+1) != str(row[2]):
     #Names.append(Poll_data[i][2])
     #Candidates_name = str[Names]



        
    
    



#List of candidates who received votes

#Percentage of votes each candidate won

#Total number of votes each candidate won

#Winner of the election based on popular votes




output = f'''
Election Results
------------------------
Total Votes: {Total_votes}
------------------------- 
Charles Casper Stockham:
Diana DeGette: 
Raymon Anthony Doane:
-------------------------
Winner: 
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