import csv
import os

# Function to analyze election data
def analyze_election_data(csv_path, output_file):
    # Initialize variables
    total_votes = 0
    candidate_votes = {}

    # Read the CSV file
    with open(csv_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip header row

        # Loop through rows in the dataset
        for row in csvreader:
            # Extract candidate name from the row
            candidate = row[2]

            # Update total votes and candidate votes
            total_votes += 1
            candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

    # Calculate the percentage of votes each candidate won
    candidate_percentages = {name: (votes / total_votes) * 100 for name, votes in candidate_votes.items()}

    # Find the winner based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)

    # Print the election results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidate_votes.items():
        print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Write results to a text file in the same directory as the script
    with open(output_file, 'w') as outfile:
        outfile.write("Election Results\n")
        outfile.write("-------------------------\n")
        outfile.write(f"Total Votes: {total_votes}\n")
        outfile.write("-------------------------\n")
        for candidate, votes in candidate_votes.items():
            outfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
        outfile.write("-------------------------\n")
        outfile.write(f"Winner: {winner}\n")
        outfile.write("-------------------------\n")

# Get the absolute path to the CSV file
csv_path = os.path.join("C:\\Users\\adamf\\OneDrive\\Desktop\\Starter_Code\\PyPoll\\Resources", "election_data.csv")

# Specify the output file path with the same directory as the script
output_file = "election_results.txt"

# Call the function to analyze the election data
analyze_election_data(csv_path, output_file)