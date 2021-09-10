# The data we need to retrieve for the election analysis.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# To use datetime as an example for uploading modules - 
    # Import datetime
        # import dateime
    # Declare the now variable to hold time right "now". The first datetime is the module,
    # the second datetime is the class, and now() is the attribute.
        # now = datetime.datetime.now()
    # Then print the date and time.
        # print("The time right now is ", now)


# import csv
# import os
# file_to_load = os.path.join("election_results.csv")
# with open(file_to_load) as election_data:
#     print(election_data)

### Direct path to the file

# # Assign a variable for the file to load and the path.
# file_to_load = "Desktop/Election_Analysis/Resources/election_results.csv"

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

# # To do: perform analysis.
#     print(election_data)

# # Close the file.
# election_data.close()

### Indirect path to the file
import csv
import os

# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Desktop", "Election_Analysis", "Resources", "election_results.csv")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

#     # Print the file object.
#     print(election_data)

### Write data to a file.

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter, set it to 0.
total_votes = 0

# Create a list to capture the candidate options. You'll add to this during the For loop below.
candidate_options = []

# Create a dictionary to tally the number of votes for each candidate. You'll use this in the For loop.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: Read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    # headers = next(file_reader)

    # Loop over the rows and count the number of total votes. Print each row in the csv file
    for row in file_reader:
        # Tally the total votes.
        total_votes += 1

        # Print all rows.
        # print(row)
    
        # Get the candidate's name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate ...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate_options list.
            candidate_options.append(candidate_name)
        
            # Start tracking each candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Increment votes for each candidate.
        candidate_votes[candidate_name] += 1
    
    # Include another loop to determine the percentage of votes for each candidate by looping 
    # through the counts.

    # Create the For loop to iterate through the candidate voting list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
            
        # Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        # Print out the winning candidate, vote count, and percentage to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winnging_count = votes and winning_percent = vote %
            winning_count = votes
            winning_percentage = vote_percentage
                # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            
    # Winning candidate summary!
    winning_candidate_summary =  (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    print(winning_candidate_summary)

    # Print the vote total.
    # print(total_votes)

    # Print the candidate options.
    # print(candidate_options)

    # Print candidate vote dictionary.
    # print(candidate_votes)

## Find the total number of candidates and list thier names.

# Declare a new list, which will inlclude the names of the candidates. Add this before
# the with open() statement above.


## Write some data to the file.
#     txt_file.write("Hello World!")

## Practice adding more text to the file.
#     txt_file.write("Arapahoe, ")
#     txt_file.write("Denver, ")
#     txt_file.write("Jefferson")

## You can add all 3 in one line like this.
#     txt_file.write("Arapahoe, Denver, Jefferson")
#     txt_file.write("Test test test")

# # Go to a new line using \n, called "newline escape sequence."
#     txt_file.write("Arapahoe\nDenver\nJefferson")

# Skill Drill: Modify code so that the output file looks like the model.
    # txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
