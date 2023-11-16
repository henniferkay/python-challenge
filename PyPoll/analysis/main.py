## poll data analysis ##

# import modules before calling in the dataset
import os
import csv

# open the csv 
polls_csv = os.path.join("..", "Resources", "election_data.csv")

# create the variables of interest and set them to certain values to start from
total_count = 0
winner = ""

# create a list to keep track of the election candidates and their respective vote counts
candidates = []
votes = []
votes_percentages = []

# create a dictionary to keep track of vote counts per candidate
candidate_count = {}

# read csv file
with open(polls_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #header row
    headers = next(csvreader)

    #start a loop that goes by row
    for row in csv.reader(csvfile):
        
        #obtain the total number of votes cast
        total_count += 1

        #list all the candidate names
        name = row[2]

        #add a new candidate to the list if different from the previous row
        if name not in candidates:
            candidates.append(name) 
            #start counting the votes per candidate
            candidate_count[name] = 0
            index = candidates.index(name)
            votes.append(0)
            #votes_percentages.append(0)
            votes[index] += 1
            #[index] = round((votes[index]/total_count)*100,3)
        else:
            index = candidates.index(name)
            votes[index] += 1
            #votes_percentages[index] = round((votes[index]/total_count)*100,3)

        #final vote count per candidate summarized in a dictionary
        candidate_count[name] += 1

# compute the statistics of the election results

    #find the winner of the election (candidate with most votes)
    winner_index = votes.index(max(votes))
    winner = candidates[winner_index]

    #percentages of vote counts for each candidate
    candidate_perc0 = round((votes[0]/total_count)*100,3) 
    candidate_perc1 = round((votes[1]/total_count)*100,3) 
    candidate_perc2 = round((votes[2]/total_count)*100,3) 

# print out the variables created above to check if the code worked successfully
print(total_count)
print(candidates)
print(votes)
print(candidate_count)
print(winner)
print(candidate_perc0)
print(candidate_perc1)
print(candidate_perc2)

# generate output summary
output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_count:,}\n"
    f"----------------------------\n"
    f"{candidates[0]}: {candidate_perc0}% ({votes[0]:,})\n"
    f"{candidates[1]}: {candidate_perc1}% ({votes[1]:,})\n"
    f"{candidates[2]}: {candidate_perc2}% ({votes[2]:,})\n"
    f"----------------------------\n"
    f"Winner: {winner}\n"
    "----------------------------\n")

# print the output
print(output)

# export the results to text file
with open("output.txt", "w") as txt_file:
    txt_file.write(output)