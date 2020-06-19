# import file
import csv
import os


file_to_load = os.path.join("Resources/election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")


# Initialize a total vote set zero:
total_votes = 0


# Declare options and candidate votes.
candidate_options = []
candidate_votes = {}


# Initalize the winning candidate, vote count, and percentage:

winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open & read the file.

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    # for row.
    for row in file_reader:

        # total vote count incrase:
        total_votes += 1
        # candidate name from each row:
        candidate_name = row[2]
        # the candidate name not in candidate options:
        if candidate_name not in candidate_options:
            # Add list.
            candidate_options.append(candidate_name)
            # for candidate votes:.
            candidate_votes[candidate_name] = 0
        # incrase list.
        candidate_votes[candidate_name] += 1

# write a result in text file:
with open(file_to_save, "w") as txt_file:

    # Print:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")


    txt_file.write(election_results)

    # vote count and percentage:
    for candidate in candidate_votes:

        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print data:
        print(candidate_results)
        txt_file.write(candidate_results)

        # find winning candidate:
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    #print data:
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #write in text file:
    txt_file.write(winning_candidate_summary)