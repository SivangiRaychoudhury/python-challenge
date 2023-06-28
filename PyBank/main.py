#import os module and csv module that allow us to create the file paths and read the csv files 
import os
import csv

#set the path for the .csv file
csvpath = os.path.join('/Users/soma/Desktop/Bootcamp/python-challenge/PyBank/Resources/budget_data.csv')

#open and read the csv file using csv module
with open(csvpath) as csvfile:
    
    #csvreader specifies the delimiter and variable that holds contents in csvfile
    csvreader = csv.reader(csvfile, delimiter = ',')    
    
    #Read the header row first
    csv_header = next(csvreader)
    
    #First month data excluding the header
    Budget_Table = [next(csvreader)]
    
    #net total amount for the first month
    Net_Total_Amount = int(Budget_Table[0][1])  
    
    #change in profit/loss for the first month
    Total_Change = 0
   
    for i in csvreader:
     #Calculating number of months
     Budget_Table.append(i)
     
     #calculate the Net total amount of profit and losses
     Net_Total_Amount = Net_Total_Amount + int(i[1])
     
     Total_months = len(Budget_Table)
    #print(f'Total months: {Total_months}')
    
    #print(f'Total: ${Net_Total_Amount}')

    for j in range(len(Budget_Table)):
        #stops the calculation at the last row  
        if j+1 == len(Budget_Table): 
           k=len(Budget_Table)-1
        else: k=j+1
     
      #changes in profit/losses over the entire period  
        Change = int(Budget_Table[k][1])-int(Budget_Table[j][1])
        
        Total_Change = Total_Change + Change
   
    #calculates the average of the changes   
    Average_Change = Total_Change/(len(Budget_Table)-1)
    #print(f'Average Change: ${Average_Change: .2f}')

 #Greatest increase in profit over the entire period
   
    
#Greatest decrease in profit over the entire period


output = f'''
Financial Analysis
--------------------------
Total months: {Total_months}
Total: ${Net_Total_Amount}
Average Change: ${Average_Change: .2f}
Greatest Increase in Profits: 
Greatest Decrease in Profits:

'''
print(output)
csvpath = os.path.join('/Users/soma/Desktop/Bootcamp/python-challenge/PyBank/Analysis/PyBank_Analysis.txt')
with open(csvpath,'w') as textfile:
 textfile.write(output)



#output
  #  Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)

