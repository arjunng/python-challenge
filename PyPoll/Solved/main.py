
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

    candidates = []
    voteList = []
    for row in csvreader:
        
        voteList.append(row[2])
        
        candidate = row[2]
        if candidate in candidates:
            next
        else:
            candidates.append(candidate)
    
    #print(voteList)
    #print(candidates)
    indCandVotes=[]
    counter=0
    for j in range(len(candidates)):
        for i in range(len(voteList)):
            if (candidates[j] == voteList[i]):
                counter+=1

            else:
                next

        indCandVotes.append(counter)
        counter=0

    #print(indCandVotes)  
    highestVotes = max(indCandVotes)
    indexofHighestVotes = indCandVotes.index(highestVotes)
    
    print("Election Results:")
    print("--"*25)
    print(f"Total Votes: {len(voteList)}")
    print("--"*25)
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {round((indCandVotes[i]/len(voteList)*100),3)}% ({indCandVotes[i]})")
    # Determining the winner of the election
    print("--"*25)
    print(f"Winning Candidate: {candidates[indexofHighestVotes]}")
    print("--"*25)

    f = open("../Output/Results.txt", 'w+')

    f.write("Election Results: \n")
    f.write("--"*25)
    f.write(f"\n Total Votes: {len(voteList)} \n")
    f.write("--"*25)
    for i in range(len(candidates)):
        f.write(f"\n {candidates[i]}: {round((indCandVotes[i]/len(voteList)*100),3)}% ({indCandVotes[i]}) \n")
    # Determining the winner of the election
    f.write("--"*25)
    f.write(f"\n Winning Candidate: {candidates[indexofHighestVotes]} \n")
    f.write("--"*25)
