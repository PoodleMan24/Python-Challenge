# importing assets
import os
import csv

#assigning location directory of csv file
budget_worksheet = os.path.join("..", "Resources", "budget_data.csv")

# assigning values to variables, to ensure they can be compared to others even while empty
totalsum = 0
totalmonth = 0
currentsum = 0
previoussum = 0
rowchange = 0
avgchange = 0
highestavg = 0
lowestavg = 0

# skipping header and setting delimiter for rows
with open(budget_worksheet) as worksheetdata:
    next(worksheetdata)
    csv_reader = csv.reader(worksheetdata, delimiter=",")
    
    # counting total of months and total summary in data set
    for rows in csv_reader:
        
        totalmonth = totalmonth + 1
        totalsum = float(rows[1]) + totalsum
        
        # finding the change of rows and then calculating the average from it
        if previoussum == 0:
            previoussum = rows[1]
        else:
            currentsum = rows[1]
            rowchange = int(currentsum) - int(previoussum)
            previoussum = rows[1]
            avgchange = avgchange + rowchange
        
        # finding the greatest increase and decrease in profits by comparing to 0, in case of workaround for lowest being above 0:
            # add new variable to check current row against previous and only update if lower than
        if rowchange > highestavg:
            highestavg = rowchange
            datehigh = rows[0]
        elif rowchange < lowestavg:
            lowestavg = rowchange
            datelow = rows[0]


# Printing headers to the terminal and text file doc
print("Financial Analysis")
print("----------------------------")    

# calculating the average change and rounding it down to 2 decimal places
longchange = avgchange/totalmonth
roundedchange = round(longchange, 2)

# printing all the information into terminal
print(f"Total # of Months: {totalmonth}")
print(f"Total: {totalsum}")
print(f"Average Change: {roundedchange}")
print(f"Greatest Increase in profits: [{datehigh}]  {highestavg}")
print(f"Greatest Decrease in profits: [{datelow}]  {lowestavg}")
print("----------------------------")

# Now we write all our answers in the same format onto a text document, this will apear in the same directory as the python code
with open("budget_data.txt", mode="wt") as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total # of Months: {totalmonth}\n")
    f.write(f"Total: {totalsum}\n")
    f.write(f"Average Change: {roundedchange}\n")
    f.write(f"Greatest Increase in profits: [{datehigh}]  {highestavg}\n")
    f.write(f"Greatest Decrease in profits: [{datelow}]  {lowestavg}\n")
    f.write("----------------------------")