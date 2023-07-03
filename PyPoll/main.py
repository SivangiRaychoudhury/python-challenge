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

    #Reads the rows excluding the header
    rows=list(csvreader)

    #Total number of votes cast 
    Total_votes=len(rows)

    #Initialising the variables
    candidate_list = []
    Votes=[]
    Percentage=[]
    Winner=[]
    Vote=0

    #List of candidates who received votes
    for i in range(Total_votes):
      if rows[i][2] not in candidate_list:
       candidate_list.append(rows[i][2])

    for j in range(len(candidate_list)):
      for i in range(Total_votes):
    #Total number and percentage of votes each candidate won 
       if rows[i][2] == candidate_list[j]:
        Vote = Vote+1   
      percent = 100*Vote/Total_votes
      Votes.append(Vote)
      Percentage.append(percent)
      #Winner of the election based on popular votes
      if Votes[j]==max(Votes):
        Winner=candidate_list[j]
      #initialize Vote and percentage for the next candidate
      Vote=0
      percent=0  

#saves the output in the given format
output = f'''
Election Results
------------------------
Total Votes: {Total_votes}
------------------------- 
{candidate_list[0]}: {Percentage[0]: .3f}% ({Votes[0]})
{candidate_list[1]}: {Percentage[1]: .3f}% ({Votes[1]})
{candidate_list[2]}: {Percentage[2]: .3f}% ({Votes[2]})
-------------------------
Winner: {Winner}
------------------------
'''

#Prints and writes the output in textfile and saves it in the given path
print(output)
csvpath = os.path.join('/Users/soma/Desktop/Bootcamp/python-challenge/PyPoll/Analysis/PyPoll_Results.txt')
with open(csvpath,'w') as textfile:
 textfile.write(output)