import os
import csv

election_path = os.path.join('..','Resources','election_data.csv')

with open(election_path, 'r') as election:
    csvreader = csv.reader(election, delimiter=',')
    
    csvheader = next(csvreader)
    
    
    print('Election Results')
    print('--------------------')

#the total number of votes cast
    def count(num):
        rowcount = 0
        for r in num:
            rowcount += 1
        return rowcount
    
    totalvotes = count(csvreader)
    print(f'Total Votes: {totalvotes}')
    print('--------------------')
    
#list of candidates who received votes
with open(election_path, 'r') as election:
    csvreader = csv.reader(election, delimiter=',')
    
    csvheader = next(csvreader)
    
   
    charles=[]
    diana=[]
    raymon=[]
    for row in csvreader:
        if row[2] == 'Charles Casper Stockham':
            charles.append(row)
        elif row[2] == 'Diana DeGette':
            diana.append(row)
        else:
            raymon.append(row)
    print(f'Charles Casper Stockham: {round(count(charles)/totalvotes*100,3)}% ({count(charles)})')
    print(f'Diana DeGette: {round(count(diana)/totalvotes*100,3)}% ({count(diana)})')
    print(f'Raymon Anthony Doane: {round(count(raymon)/totalvotes*100,3)}% ({count(raymon)})')
    print('--------------------')    

#print out the winner
    # def max(num):
    #     x = 0
    #     for r in num:
    #         if r > x:
    #             x=r
    #     return x
    

    summary = {'Charles Casper Stockham':count(charles), 'Diana DeGette':count(diana), 'Raymon Anthony Doane':count(raymon)}
    x=0
    y=0
    for name, sum in summary.items():
        if sum > x:
            x = sum
            y = name
    print(f'Winner: {y}')

    print('--------------------')
    
    

    
    