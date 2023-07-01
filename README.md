#PYTHON-CHALLENGE:

Two challenges are completed using the Python script.

#INITIAL STEPS TAKEN
- A new repository "python-challenge" is created in GitHub.
- Cloned the repository to my computer.
- Inside the local repository, two folders are created "PyBank" and "PyPoll".
- Inside each assignment folder are the following:
   1. main.py -> file that holds the python script for the analysis
   2. Resources -> folder containing the .csv file which is used for the analysis.
   3. Analysis -> folder containing the text file with the output from the analysis.
 
 - Pushed to the GitHub.
 
 #PYBANK ANALYSIS
 
 For this challenge, a python script is created that analyzes the dataset, budget_data.csv and calculated the following:
 
  1. The total number of months included in the dataset
  2. The net total amount of "Profit/Losses" over the entire period
  3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
  4. The greatest increase in profits (date and amount) over the entire period
  5. The greatest decrease in profits (date and amount) over the entire period

- Finally, the script prints the output of the analysis to the terminal and exports it to a text file.

The analysis gives the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)


#PYPOLL ANALYSIS

For this challenge, a python script is created that analyzes the dataset, election_data.csv and calculated the following:

  1. The total number of votes cast
  2. A complete list of candidates who received votes
  3. The percentage of votes each candidate won
  4. The total number of votes each candidate won
  5. The winner of the election based on popular vote
  
- Finally, the script prints the output of the analysis to the terminal and exports it to a text file.

The analysis yields the following output:

Election Results
------------------------
Total Votes: 369711
------------------------- 
Charles Casper Stockham:  23.049% (85213)
Diana DeGette:  73.812% (272892)
Raymon Anthony Doane:  3.139% (11606)
-------------------------
Winner: Diana DeGette
------------------------

