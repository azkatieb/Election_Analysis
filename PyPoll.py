# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote



# Assign a variable for the file to load and the path.
# Python not running in script directory full path used - relative path does not currently work
file_to_load = '/Users/katiebernstein/Documents/Data Bootcamp/Git/Election_Analysis/Resources/election_results.csv'


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("/Users/katiebernstein/Documents/Data Bootcamp/Git/Election_Analysis/analysis/", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Open the election results and read the file 
with open(file_to_load,'r') as election_data:

    # to do: perform analysis
    print(election_data)

# close the file
election_data.close()

