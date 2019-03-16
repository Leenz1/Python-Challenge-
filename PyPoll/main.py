
import csv 
import statistics 
py =r"/Users/harleenshah/Desktop/UCDSAC201902DATA4/03-Python/Homework/Instruction/PyPoll/Resources/election_data.csv" 
with open(py, newline='') as pyCSV:
    Candidate= []
    VoteCounter= []
    rowcount= 0
    Winner= 0
    WinnerName= ""
i = 0
with open(py, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    for row in csvreader:
        
        rowcount = rowcount + 1
        if row[2] not in Candidate:
            Candidate.append(row[2])
            VoteCounter.append(0)
        else:
            VoteCounter[Candidate.index(row[2])] = VoteCounter[Candidate.index(row[2])] + 1

            
Winner = max(range(len(VoteCounter)), key = lambda x: VoteCounter[x])
WinnerName = Candidate[int(Winner)]
print("Election Results are in!")
print("-----------------")
print("Total Votes: " + str(rowcount))
print("--------------------")
while i <= (len(Candidate) - 1):
    print(Candidate[i] + ": " + str(round((VoteCounter[i]/rowcount * 100),2)) + "% (" + str(VoteCounter[i]) + ")")
    i = i + 1
print("---------------------")
print("Winner: " + str(WinnerName))
print("--------------------------")
            
