import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")
candidate = []
candidate_votes = []
total_votes = 0

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    for row in csvreader:
        if len(candidate) == 0:
            candidate.append(row[2])
            candidate_votes.append(1)
            total_votes += 1 
        elif row[2] in candidate:
            total_votes += 1
            candidate_votes[candidate.index(row[2])] += 1
        else:
            candidate.append(row[2])
            candidate_votes.append(1)
            total_votes += 1


print("Election Results"
    + "\n-------------------------"
    + "\nTotal Votes: " + str(total_votes) 
    + "\n-------------------------" 
    + "\n" + candidate[0] + ": " + str(round(100 * (candidate_votes[0] / sum(candidate_votes)), 3)) +"% (" + str(candidate_votes[0]) +")"
    + "\n" + candidate[1] + ": " + str(round(100 * (candidate_votes[1] / sum(candidate_votes)), 3)) +"% (" + str(candidate_votes[1]) +")" 
    + "\n" + candidate[2] + ": " + str(round(100 * (candidate_votes[2] / sum(candidate_votes)), 3)) +"% (" + str(candidate_votes[2]) +")"
    + "\n-------------------------"
    + "\nWinner: " + candidate[candidate_votes.index(max(candidate_votes))])

with open("election_analysis.txt", 'w') as file:
    file.write("Election Results")
    file.write("\nTotal Votes: " + str(total_votes)) 
    file.write("\n" + candidate[0] + ": " + str(round(100 * (candidate_votes[0] / sum(candidate_votes)), 3)) +"% (" + str(candidate_votes[0]) +")")
    file.write("\n" + candidate[1] + ": " + str(round(100 * (candidate_votes[1] / sum(candidate_votes)), 3)) +"% (" + str(candidate_votes[1]) +")" )
    file.write("\n" + candidate[2] + ": " + str(round(100 * (candidate_votes[2] / sum(candidate_votes)), 3)) +"% (" + str(candidate_votes[2]) +")")
    file.write("\nWinner: " + candidate[candidate_votes.index(max(candidate_votes))])