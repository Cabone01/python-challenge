# Python Challenge
This folder contains two the python assignments that were done and their scripts, csv files, and txt files.  
    
## PyBank
In this folder a csv file containing the records of a company which were the date and profits/losses. 
So with python I counted the how many months their were by simply counting each row since the data was recorded monthly.
The total difference between each profit/loss was from one month to the next was gotten then averaged at the very end.
To get the greatest profit increase I add to have a maximum variable set to the lowest value. Then going through each row I checked if the net change was greater 
then the max and if it was then max variable would be replaced with the new maximum.
For the greatest profit decrease I basically did the same as max but intead check if it was smaller.
    
## PyPoll
This folder contained the csv file of election results with the data consisting of voter id, county, and candidate.
I had set variables to check the total votes, list of candidates, list of candidates votes.
To make sure I was counting the correct amount of votes for each candidate when going through each row of the csv file, I checked if the candidate name was in the list.
If it was not then I would append it to the candidate list and add one vote to the candidate. If it was then I would find the index it was in the list and add the vote
in the candidate votes list with that index.
After all the I printed the list out and created a txt file with it. I had the votes divided by the total, multiplyed by 100, and rounded to three decimal points when printing them.
