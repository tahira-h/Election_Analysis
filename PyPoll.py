# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote. 

#Create a filename variable to a direct or indirect path to the file. 
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode to write data to the file.
# open(file_to_save, "w")


#Create a filename variable to a direct or indirect path to the file. 
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file. 
#outfile.write("Hello World")

#Close the file
# outfile.close()

# Add our dpendencies
import csv 
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

 # Print the candidate name from each row.
        candidate_name = row[2]

# Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

# 3. Print the total votes.
print(total_votes)


    #Print the file object.
#    print(election_data)

# Initialize a total vote counter
total_votes = 0

# Candidate options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)
# Close the file. 
election_data.close()

# Open the election results and read the file. 
#with open(file_to_load) as election_data:
#    file_reader = csv.reader(election_data)

#Read the header row.
#headers = next(file_reader)

# Print each row in the CSV file.
for row in file_reader:
    # Add to the total vote count.
    total_votes += 1

    # Get the candidate name from each row.
    candidate_name = row[2]

    # If the candidate does not match any existing candidate...
    if candidate_name not in candidate_options:

        # Add it to the list of candidates.
        candidate_options.append(candidate_name) 

        # Add begin tracking that candidate's vote count.
        candidate_votes[candidate_name] = 0

    # Add a vote to that candidate's count.
    candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")

        # Save the final vote count to the text file.
        txt_file.write(election_results)
        for candidate_name in candidate_votes:
            # Retrieve vote count and percentage.
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100

    # Print each candidate, their voter count, and percentage to the terminal. 
   # print(f"{candidate_name}: {vote_percentage:.1f}% ({vote:,})\n")
    candidate_results = (
        f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

    # Print each candidate, their voter count, and percentage to the terminal.
    print(candidate_results)
    # Save the candidate results to our text file.
    txt_file.write(candidate_results)

    # Determine winning vote count and candidate
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

# Print the winning candidate's results to the terminal
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winnin_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"-------------------------")
print(winning_candidate_summary)
    
# Save the winning candidate's results to the text file.
txt_file.write(winning_candidate_summary)


