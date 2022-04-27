# add our dependencies
import csv
import os

# assign a variable for the file to load from a path
file_to_load = "Resources/election_results.csv"
# open the election results and read the file
election_data = open(file_to_load, 'r')

# to do: perform analysis

# close the file
election_data.close()

# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The % number of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
