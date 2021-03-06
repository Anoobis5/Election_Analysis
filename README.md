# Election_Analysis
A code to analyze an election audit data set. 

## Overiew of the Election Audit
A Colorado Board of Elections employee has give the following tasks to complete the elction audit of a recent local congressional election:

1. Calculate how many votes were cast in this congressional election.
2. Provide a breakdown of the number of votes and the percentage of total votes for each county.
3. Calculate which county had the largest number of votes.
4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
5. Determine which candidate won the election, what was their vote count, and what was their percentage of the total votes was.


## Resoruces used in analysis
* Data Source: election_results.csv
* Software: Python 3.7.6, Visual Studio Code, 1.57.1

## Election Audit Results
By Using Python and analyzing the CSV data set provided, we were able to code calculations, conditional statements, and loops to identify the data requested by the Colorado Board of Elections. Our analysis of the election data showed us that:


* **There were "369,711" votes cast in the election.**

* **Counties in the election & their voter turnout breakdown:**
  * **Jefferson county** with 38,855 votes (10.5%)
  * **Denver county** with 306.055 votes (82.8%)
  * **Arapahoe with** with 24,801 votes (6.7%)

* **Denver county had the largest voter turnout with 306,005 votes, at 82.8% of the total votes cast.**

Please see below for the code format that helped us analyze this data:

![County_Loop](https://user-images.githubusercontent.com/84881187/123560910-3bd5a480-d773-11eb-8372-d5d7d130fe6c.PNG)
![County_Vote_and_Largest](https://user-images.githubusercontent.com/84881187/123560919-4859fd00-d773-11eb-8b12-8ff673b63172.PNG)


 ## Election Audit Results
 
 * **The candidates in the election were:**
  1. Charles Casper Stockham
  2. Diana DeGette
  3. Raymon Anthony Doane
 

**After we processed the data, the results of the election were:**
 
  * **Charles Casper Stockham** received 23.0% of the vote and 85,213 votes.
  * **Diana Degette received** 73.8% of the vote and 272,892 votes.
  * **Raymon Anthony Doane** received 3.1% of the vote and 11,606 votes.
   
**The winner of the election was:**
  * **Diana Degette**, who received "73.8%" of the vote and "272,892" votes.

Our code below enabled us to total the votes for each candidate from each count to help us determine the winner:
 
![Candidate](https://user-images.githubusercontent.com/84881187/123560885-18125e80-d773-11eb-889f-ff10aa8b06a4.PNG)

![Candidate_County_Loop_2](https://user-images.githubusercontent.com/84881187/123560989-cc13e980-d773-11eb-98db-96812d869517.PNG)


## Election Audit Summary
The election commission has requested we delve further into the analysis of the CSV election data set. They requested we analyze the number of votes cast from each county, and calculate the percentage of votes from each county in the election. They also wished to determine which county had the largest voter turnout. We used Python and Visual Studio Code in conjunction with Git to write and upload this script in order analyze this, and any future elections. Please see below for our code format that enabled us to extract the data from the CSV set to analyze:

![Candidate_County_Loop](https://user-images.githubusercontent.com/84881187/123560954-848d5d80-d773-11eb-966e-7a7333665c45.PNG)


By using Python and VSCode instead of Excel, we were able to write descriptive "pseudocode" that can easily be interpreted for future coders and users. The writeen code allows for variable entry of non-specific candidate and counties, which will allow for this code to be used in any future election audits' CSV data sets to find their totals and winner.

If the auditor and coders wishes to delve deepter into more specific variables collected in future data sets, such as voter demographic, age, race/ethnicity, etc., they will need to refactor the code to include those variables. Fortunately, our code structure has indexed data loops they can use as a foundation for adding those values to the existing code. Our script is variable in naming, but still focuses on the election data's candidates and counties. If one wished to expand to a much larger data set to include demographics across a larger geographic region (such as cities and states), the code would need to be modified to reflect the new data set. Thankfully, since our code is readable and flexible, the refactoring process is pretty minimal. 


