## Election_Analysis
### Project Overview
The following audit addresses the tasks listed immediately below. The purpose of the analysis was to uplift key findings from a recent congressional election for the Colorado Board of Elections.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Calculate the voter turnout for each county.
6. Calculate the percentage of votes from each county out of the total votes.
7. Determine the county with the highest turnout.
8. Determine the winner of the election based on popular vote.

### Resources
* Data Source: election_results.csv
* Software: Python 3.6.1, Visual Studio Code, 1.38.1

### Summary
The analysis of the election shows that:

* There were 369,711 votes cast in the election.
* In terms of votes cast by county:
	* Jefferson County cast 38,855 votes (10.5% of the total)
	* Denver County cast 306,055 votes (82.8% of the total)
	* Arapahoe County cast 24,801 votes (6.7% of the total)
* Denver County had the highest turnout, with 306,055 votes cast, which constituted 82.8% of the election's total votes
* The candidates were:
	* Charles Casper Stockham
	* Diana DeGette
	* Raymon Anthony Doane
* The candidate results were:
	* Stockham received 23% of the vote and 85,213 number of votes.
	* DeGette received 73.8% of the vote and 272,892 number of votes.
	* Doane received 3.1% of the vote and 11,606 number of votes.
* The winner of the election was:
	* Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

### Election-Audit Summary
Though this analysis was specific to a single election in Colorado, the script can be repurposed to uplift insights from data for other voting cycles. The field for "candidate" in the source data can easily be repopulated with individuals running in other elections, be they at the local, state, or national level. In those cases, the "county" field could be replaced with different jurisdiction types, such as district, city, and state.

Further, the "candidate" field could be replaced with voter preferences if analyzing the results from proposition-based elections. The options "yes" and "no" would replace the candidate names in that scenario. Changes to the script would need to be made to rename variables to ensure they accurately describe the information being used (for instance, "prop_options" would replace "candidate_name). However, the syntax and functions would remain the same.

Of course, with additional fields, one could conduct significantly more complex analyses for elections. For instance, a common interest for political scientists and party leaders is how voter demographics correlate with voting decisions. Should those demographics be made available via additional fields, future analyses could yield findings such as:

* Candidate vote-share by voter race, gender, education status, and urbanicity
* Breakdown of voter preferences by age for each county
* Partisan turnout by county

Analysts would need to add additional script featuring new lists and dictionaries to work with these fields.



