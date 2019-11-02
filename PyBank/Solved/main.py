
# Importing key libraries
import os
import csv

# Declaring the csv file
file = os.path.join("..", "Resources","03-Python_Instructions_PyBank_Resources_budget_data.csv")

# Reading the CSV file into the csvreader
with open(file, newline = '') as csvFile:

    csvreader = csv.reader(csvFile)
    csvreader1 = csv.reader(csvFile)

    csv_header = next(csvreader)

    # Variable to store the number of rows in the CSV file
    totalMonths = 0

    # Variable to store overall profit loss
    finalBal = 0

    # List to store the profit/loss column 
    pllist = []
    datelist=[]

    # Looping through the csv reader to calculate length, overall profit and to 
    # build the two new lists - datelist and profit/loss list   
    
    for row in csvreader:

        finalBal += int(row[1])
        totalMonths += 1
        datelist.append(row[0])
        pllist.append(row[1])

    #print(datelist)

    # Variable declaration to store difference and differenceprofitloss

    differencepl=0
    difference=0

    # Declaring a list of store differences
    diffList=[]

# Looping to build the differences list
    for i in range(len(pllist)-1):
        diffList.append(int(pllist[i+1])-int(pllist[i]))

    #print(diffList)

    sum=0
    # Loop to calculate sum of differences to find average
    for i in range(len(diffList)):
        sum += diffList[i]

    # Average profit loss calculation
    averageprofitloss = sum/len(diffList)

    # print(len(diffList))
    
    # for i in range(len(pllist)-1):
    #     difference=int(pllist[i+1])-int(pllist[i])
    #     differencepl += difference
    
    # #print(differencepl)
    # averageprofitloss = differencepl/(len(pllist)-1)
    
    maxProfit = max(diffList)
    maxLoss = min(diffList)

    maxProfitMonth = datelist[diffList.index(maxProfit)+1]
    maxLossMonth = datelist[diffList.index(maxLoss)+1]

    print("Financial Analysis:")
    print("--"*25)
    print(f"Total Months: {totalMonths}")
    print(f"Total profit: {finalBal}")
    print(f"Average Change: {averageprofitloss}")
    print(f"Greatest Increase in Profits: {maxProfitMonth}(${maxProfit})")
    print(f"Greatest Decrease in Profits: {maxLossMonth}(${maxLoss})")

f = open("../Output/Results.txt","w+")

f.write("Financial Analysis: \n")
f.write("------------------------------------------------ \n")
f.write(f"Total Months: {totalMonths} \n")
f.write(f"Total profit: {finalBal} \n")
f.write(f"Average Change: {averageprofitloss} \n")
f.write(f"Greatest Increase in Profits: {maxProfitMonth}(${maxProfit}) \n")
f.write(f"Greatest Decrease in Profits: {maxLossMonth}(${maxLoss}) \n")


