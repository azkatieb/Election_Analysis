# **Election Analysis Module 3 Challenge**

## **Overview of Election Audit**

Colorado Board of Elections employees Seth and Tom have requested an audit of the election data which includes the following results:

- total number of votes cast.
- list of candidates who received votes.
- total number of votes each candidate received.
- percentage of votes each candidate won.
- winner of the election based on popular vote.
- voter turnout for each county.
- percentage of votes from each county out of the total count
- county with the highest turnout 

By reviewing the results, it will ensure we are using clean data and the results are checked and verified and the winners can be announced. Auditing is an important practice to check all of the data being used and checking the results multiple times to ensure no errors have occurred. 

### Resources Used:
Data Source: election_results.csv
Software: Python 3.9.12
## **Election Audit Results**

- Total number of votes cast: 
     - 369,711
- All Candidates, Percentage of Votes and Total Votes:
     - Charles Casper Stockham: 23.0% (85,213)
     - Diana DeGette: 73.8% (272,892)
     - Raymon Anthony Doane: 3.1% (11,606)
- Winner of the election based on popular vote:
    - Winner: Diana DeGette
    - Winning Vote Count: 272,892
    - Winning Percentage: 73.8%
- County Votes and Percentage of Total Votes:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
- County with the highest turnout:
        - Denver (306,055 votes)


## **Election Audit Summary**
The process we used to audit the election results can be used in the future for many other elections as the basic structure of the code we used can be modified depending of the csv data provided and the calculations needed. 

For instance, if the election results csv file had the data loaded into different columns then you could go to the code and modify the lines 51 and 54 to use the new column index number. Remember that the column index starts at 0 so if the data for candidate name was in column 5 this time versus 3 for our data set, you would put 4 in [4] for line 51. This would be the same for county name etc, whenever you are referring to data from a specific column, you would need to ensure the index is referring to the column in your new csv file with the correct data. 

Another way you could script for other elections would be if you were compiling the results for a city or county election versus a state election and wanted to look at more subsets of data, you could follow the format we used in lines 38 to 80 to convert the data in your new csv file to a list of new dicitonaries that will be important for your analysis of that specific election. Such as using city names versus county names or using proposition numbers instead of candidate names. 

The basic structure of this election analysis will help in many different types of elections and by changing dictionaries or reference columns you will be able to use this script many times without having to rewrite the script each time. 
