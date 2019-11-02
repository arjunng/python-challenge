
# Importing the necessory libraries

import os
import csv
import math

# Declaring the csv file path

file_path = os.path.join("..", "Resources", "03-Python_Instructions_PyPoll_Resources_election_data.csv")

# Dictionary declaration
myDict = {}

#Reading the csvfile

with open(file_path, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    candVotes = []
    for row in csvreader:
        candVotes.append(row[2])
    # Getting the values from column Votes into a dictionary
        myDict[row[2]]=0

    #print(candVotes)

    # Converting the dictionary keys into the candidate list
    candlist = []
    for i in myDict.keys():
        candlist.append(i)

    #print(candlist)
    # Initializing candidate votes to 0
    candidateVotes = [0,0,0,0]

    # Counting votes
    for i in candVotes:
        if i == candlist[0]:
            candidateVotes[0]+=1
        elif i == candlist[1]:
            candidateVotes[1]+=1
        elif i == candlist[2]:
            candidateVotes[2]+=1
        else:
            candidateVotes[3]+=1
    
    wpCand1 = (candidateVotes[0]/len(candVotes))*100
    wpCand2 = (candidateVotes[1]/len(candVotes))*100
    wpCand3 = (candidateVotes[2]/len(candVotes))*100
    wpCand4 = (candidateVotes[3]/len(candVotes))*100

    highestVotes = max(candidateVotes)
    indexofWinningCandidate=candidateVotes.index(highestVotes)

    print("Election Results:")
    print("--"*25)
    print(f"Total Votes: {len(candVotes)}")
    print("--"*25)
    print(f"{candlist[0]}: {round(wpCand1,3)}% ({candidateVotes[0]})")
    print(f"{candlist[1]}: {round(wpCand2,3)}% ({candidateVotes[1]})")
    print(f"{candlist[2]}: {round(wpCand3,3)}% ({candidateVotes[2]})")
    print(f"{candlist[3]}: {round(wpCand4,3)}% ({candidateVotes[3]})")
    # Determining the winner of the election
    print("--"*25)
    print(f"Winning Candidate: {candlist[indexofWinningCandidate]}")
    print("--"*25)

    f = open("../Output/Results.txt", 'w+')

    f.write("Election Results: \n")
    f.write("--"*25)
    f.write(f"\n Total Votes: {len(candVotes)} \n")
    f.write("--"*25)
    f.write(f"\n {candlist[0]}: {round(wpCand1,3)}% ({candidateVotes[0]}) \n")
    f.write(f"{candlist[1]}: {round(wpCand2,3)}% ({candidateVotes[1]}) \n")
    f.write(f"{candlist[2]}: {round(wpCand3,3)}% ({candidateVotes[2]}) \n")
    f.write(f"{candlist[3]}: {round(wpCand4,3)}% ({candidateVotes[3]}) \n")
    # Determining the winner of the election
    f.write("--"*25)
    f.write(f"\n Winning Candidate: {candlist[indexofWinningCandidate]} \n")
    f.write("--"*25)
