# Election_Analysis

Project overview:
--------------------------------------------
Coloarado Board of Elections 'task.I need for perfome on follwing task.

1 calculate the total number of vote.

2 Get  total candidate.

3 calculate total number of candidates who received votes.

4 calculate percentage of votes each candidate won.

5 find a winner based votes.

Resources:
----------------------------------------------

election_results.csv

software:python,visual studio code

Summary:
------------------------------------------------
 
 
    Election Results
    -------------------------
    Total Votes: 369,711
    -------------------------
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    -------------------------
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    -------------------------
Challenge
------------------------------------------------
I got challenge for Election_Analysis.I need to use for loops and conditional statements to calculate the voter turnout for each county as well as the percentage of votes each county contributed to the election. Then, determine which county had the largest turnout.

Summary_challenge code:
--------------------------------------------------

After Completed challenge a code look like that:



    # import file
    import csv
    import os


    file_to_load = os.path.join("Resources1","election_results.csv")

    file_to_save = os.path.join("analysis_challenge", "election_analysis1.txt")


    # Initialize a total vote set zero:
    total_votes = 0

    # Declare candidate options , candidate votes , county options and county votes::
    candidate_options = []
    candidate_votes = {}
    county_options = []
    county_votes = {}

    # open and read files:
    with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)
        headers = next(file_reader)
        # looking into row:
        for row in file_reader:
          # add totalvotes:
          total_votes += 1

      # for county:
      #county index value =1
      county_name = row[1]
      if county_name not in county_options:
        # append use for add list:
        county_options.append(county_name)

        county_votes[county_name] = 0
      #list add:
      county_votes[county_name] += 1
      # For candidate:
      candidate_name = row[2]
      if candidate_name not in candidate_options:
        # use append for incrase list:
        candidate_options.append(candidate_name)
        #sets value to zero:
        candidate_votes[candidate_name] = 0
      # incrase list:
      candidate_votes[candidate_name] += 1


    # Initalize the  value for candidate and county:

    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    winning_county = ""
    winning_county_count = 0
    winning_county_percentage = 0

    #save and write data in files:
    with open(file_to_save, "w") as txt_file:

      # Print election results:
      election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n"
          f"County Votes:\n")
      print(election_results, end="")

      # Save file:
      txt_file.write(election_results)

      # for county votes:
      for county in county_votes:
        # counts votes:
        c_votes = county_votes[county]
        c_vote_percentage = float(c_votes)/float(total_votes) * 100
        county_results = (
          f"{county}: {c_vote_percentage:.1f}% ({c_votes})\n"
        )
        # print county results:
        print(county_results)
        # write  in text file:
        txt_file.write(county_results)

        # find largest county turnover:
        if c_votes > winning_county_count:
          winning_county_count = c_votes
          winning_county = county

      winning_county_summary = (
        f"-------------------------\n"
        f"Largest county turnout: {winning_county}\n"
        f"-------------------------\n"
      )
      # print :
      print(winning_county_summary)
      # write  in text file:
      txt_file.write(winning_county_summary)

      # for candidate:
      for candidate in candidate_votes:

        votes = candidate_votes[candidate]
        #find percentage:
        vote_percentage = float(votes)/float(total_votes) * 100

        # print :
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # print  results:
        print(candidate_results)
        #write in files:
        txt_file.write(candidate_results)

          # find from loop:
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate


      winning_candidate_summary = (
          f"----------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"--------------------------------\n"
      )
      #print results:
      print(winning_candidate_summary)
      #write in files:
      txt_file.write(winning_candidate_summary)
      
      
  Summary for Challenge results:
  ---------------------------------------

      Election Results
    -------------------------
    Total Votes: 369,711
    -------------------------
    County Votes:
    Jefferson: 10.5% (38855)
    Denver: 82.8% (306055)
    Arapahoe: 6.7% (24801)
    -------------------------
    Largest county turnout: Denver
    -------------------------
    Charles Casper Stockham: 23.0% (85,213)
    Diana DeGette: 73.8% (272,892)
    Raymon Anthony Doane: 3.1% (11,606)
    ----------------------------
    Winner: Diana DeGette
    Winning Vote: 272,892
    Winning Percentage: 73.8%
      
  
