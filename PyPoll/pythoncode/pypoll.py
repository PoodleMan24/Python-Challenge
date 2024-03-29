# importing assets
import os
import csv

#assigning location directory of csv file
pypoll_sheet = os.path.join("..", "Resources", "election_data.csv")

# Defining integer variables
total = 0
charles = 0
diana = 0
raymon = 0
errors = 0
charlesperc = 0
dianaperc = 0
raymonperc = 0

# assigning Candidates names as static string variables:
NAMEchar = "Charles Casper Stockham"
NAMEdia = "Diana DeGette"
NAMEray = "Raymon Anthony Doane"
bar = "-------------------------"


# skipping header and setting delimiter for rows
with open(pypoll_sheet) as worksheetdata:
    next(worksheetdata)
    csv_reader = csv.reader(worksheetdata, delimiter=",")
    
    # Starting a for loop to check each row 
    for rows in csv_reader:
        
        #calculating total amount of votes
        total = total + 1

        # Creating If statements to find what candidate was picked and adding to total for that candidate
        if rows[2] == NAMEchar:
            charles = charles + 1
        elif rows[2] == NAMEdia:
            diana = diana + 1
        elif rows[2] == NAMEray:
            raymon = raymon + 1
        else:
            errors = errors + 1

# Using if statement to determine the winner of the election
if raymon > diana and raymon > charles:
    winner = NAMEray
elif diana > raymon and diana > charles:
    winner = NAMEdia
else:
    winner = NAMEchar


# Rounding down to 3rd decimal place as well as giving a percentage answer from the total of votes
charlesperc = (charles/total)*100
cpercent = round(charlesperc, 3)
dianaperc = (diana/total)*100
dpercent = round(dianaperc, 3)
raymonperc =  (raymon/total)*100
rpercent = round(raymonperc, 3)

# Printing results
print("Election Results")
print(bar)
print(f"Total Votes: {total}")
print(bar)
print(f"Charles Casper Stockham:  {cpercent}%   [{charles}]")
print(f"Diana DeGette:            {dpercent}%   [{diana}]")
print(f"Raymon Anthony Doane:     {rpercent}%   [{raymon}]")
print(bar)
print(f"Winner: {winner}")
print(bar)

# Accounting for errors in reading Candidate column, if error occured would likely either print each row with the issue or format names into lower or uppercase
if errors > 0:
    print(f"Please check data as we have found '{errors}' errors in looking for the candidate name")
    print("Please add line of code to resolve this issue if it occurs")

# Making a text document if one doesnt exist and updating it, this should be located in same location as the python code
with open("electoral_results.txt", mode="wt") as f:
    f.write("Election Results\n")
    f.write(f"{bar}\n")
    f.write(f"Total Votes: {total}\n")
    f.write(f"{bar}\n")
    f.write(f"Charles Casper Stockham:  {cpercent}%   [{charles}]\n")
    f.write(f"Diana DeGette:            {dpercent}%   [{diana}]\n")
    f.write(f"Raymon Anthony Doane:     {rpercent}%   [{raymon}]\n")
    f.write(f"{bar}\n")
    f.write(f"Winner: {winner}\n")
    f.write(f"{bar}\n")