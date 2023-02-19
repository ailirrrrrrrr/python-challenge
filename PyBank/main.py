import os
import csv

budget_path = os.path.join('..', 'Resources', 'budget_data.csv')

with open(budget_path, 'r') as budget:
    csvreader = csv.reader(budget, delimiter=',')
    
    csvheader = next(csvreader)

    print('Financial Analysis')
    print('-------------------')

#total number of months included in the dataset
    def count(num):
        rowcount = 0
        for r in num:
            rowcount += 1
        return rowcount
    
    print(f'Total Months: {count(csvreader)}')

#total net total amount of "Profit/Losses"
with open(budget_path, 'r') as budget:
    csvreader = csv.reader(budget, delimiter=',')
    
    csvheader = next(csvreader)


    def sum(num):
        totalsum = 0
        for t in num:
            totalsum += t
        return totalsum
    
    profit = []
    for row in csvreader:
        net = int(row[1])
        profit.append(net)
    
    print(f'Total: ${sum(profit)}')


#total changes in "Profit/Losses" 
with open(budget_path, 'r') as budget:
    csvreader = csv.reader(budget, delimiter=',')
    
    csvheader = next(csvreader)

    def average(num):
        length = len(num)
        total = 0
        for r in num:
            total += r
        return total / length    

    index=0
    change=[]
    for r in profit:
        if index <= len(profit)-2:
            c = profit[index+1] - r
            change.append(c)
            index +=1
    print(f'Average Change: ${round(average(change),2)}')
   
#Greatest increase & decrease in profits
    def max(num):
        x = 0
        for r in num:
            if r > x:
                x=r
        return x
    
    def min(num):
        x = 0
        for r in num:
            if r < x:
                x=r
        return x
    
    datelist = []
    for row in csvreader:
        datelist.append(row[0])
    
    #make dictionary of date vs. change profits
    changetwo = change.copy()
    changetwo.insert(0,0)
    datecha = {}
    for d in datelist:
        for c in changetwo:
           datecha[d] = c
           changetwo.remove(c) 
           break
    
    
    for a in datecha:
        if datecha[a] == max(change):
            print(f'Greatest Increase in Profits: {a} (${max(change)})')
    
    for a in datecha:    
        if datecha[a] == min(change):
            print(f'Greatest Decrease in Profits: {a} (${min(change)})')

    
    



    

