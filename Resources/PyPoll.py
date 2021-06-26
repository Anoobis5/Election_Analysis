#1. The data we need to retrieve.
file_to_load='Desktop/Election_Analysis/Resources/election_results.csv'

#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to the file to save.
file_to_save= os.path.join("analysis","election_analysis.txt")

#Initialize a total vote counter
total_votes = 0
#Candidate options
candidate_options = []
candidate_votes = {}

#Winning Candidate and WInning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Print the header row/
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count (out of 'if' suite)
        candidate_votes[candidate_name] += 1
    
    #Determine the percentage of votes for each candidate by looping through the counts
    #Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes)*100

    
        #Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        #Determine winning voute count and candidate
        #Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percentage =
            #vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    
        winning_candidate_summary = (
            f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winner Vote Count: {winning_count:,}\n"
            f"WInning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
        print(winning_candidate_summary)
    



#2. The total number of votes cast.
#3. A complete list of candidates who received votes.
#4. The percentage of votes each candidate won.
#5. The total number of votes each candidate won.
#6. The winner of the election based on popular vote.   