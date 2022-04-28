# add our dependencies
import csv
import os

# assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")

# assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# 1. Create a county list andd county votes dictionary
county_options = []
county_votes = {}

#track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2. Track the largest county and coybty voter turnout
largest_county_turnout = ""
largest_number_turnout = 0

# open the election results and read the file
with open(file_to_load) as election_data:
   reader = csv.reader(election_data)

   # Read the header row
   headers = next(reader)

   # For each row in the CSV file
   for row in reader:

      # add to the total vote count
      total_votes = total_votes + 1

      # get the candidate name from each row
      candidate_name = row[2]

      # 3. Extract the county name from each row
      county_name=row[1]

      # if the candidate does not match any existing candidate, add it to the candidate list
      if candidate_name not in candidate_options:

         #add the candidate name to the candidate list
         candidate_options.append(candidate_name)

         #begin tracking that candidate's voter count
         candidate_votes[candidate_name] = 0

      # add a vote to that candidate's count
      candidate_votes[candidate_name] += 1

      # 4a: write a decision statement that checks the county does not match any existing county in county list
      if county_name not in county_options:

         # 4b: add the existing county to the list of counties
         county_options.append(county_name)

         # 4c: begin tracking the county's vote count
         county_votes[county_name] = 0

      # 5: add a vote to that county's vote count
      county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

   # Print the final vote count (to terminal)
   election_results = (
      f"\nElection Results\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes:,}\n"
      f"-------------------------\n\n"
      f"County Votes:\n")
   print(election_results, end="")

   txt_file.write(election_results)

# 6a: write a repetition statement to get the county from the county dictionary
for county_name in county_votes:

   # 6b: retrieve the county vote count
   vote_county = county_votes[county_name]
   # 6c: calculate the percent of total votes for the county
   vote_county_percentage = float(vote_county) / float(total_votes) * 100

   #6d: print county results to the terminal
   county_results = (f"{county_name}: {vote_county_percentage:.1f}% ({vote_county:,})\n")
   print(county_results)

   # 6e: save the county votes to a text file
txt_file.write(county_results)

   #6f: determine the winning county and get its vote count
if (vote_county > winning_count):
   winning_count = vote_county
   largest_county_turnout = county_name

# 7: Print the county with the largest turnout to the terminal.
largest_county_results = (
   f"\n"
   f"----------------------------------------\n"
   f"Largest County Turnout: {largest_county_turnout}\n"
   f"----------------------------------------\n")
print(largest_county_results)

# 8: save the final candidate vote count to the text file
winning_count = 0
for candidate_name in candidate_votes:
   #retrieve vote count and %
   votes = candidate_votes.get(candidate_name)
   vote_percentage = float(votes)/float(total_votes)*100
   candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
