#main for pybank
#import dependencies
import os
import csv

#create the path for file
bankpath = os.path.join('Resources', 'budget_data.csv')

Month_Dates = []
Month_PL = []
Total_net = 0

#Read file
with open(bankpath, 'r') as bankfile:

    bank_file_reader = csv.reader(bankfile)

    #Skip header row
    next(bank_file_reader)

    Total_months = 0
    Total_profit_loss = 0

    for rows in bank_file_reader:
        #For the first two lines, count number of rows to give us the number of months. Add row 1 for profit
        Total_months = Total_months + 1
        Total_profit_loss = Total_profit_loss + int(rows[1])

        
        Month_Dates.append(str(rows[0]))
        Month_PL.append(int(rows[1]))

    greatest_increase = Month_PL[0]
    lowest_drop = Month_PL[0]

    #Find the greatest/lowest months
    for i in range(len(Month_PL)):

        if Month_PL[i] > greatest_increase:
                greatest_increase = Month_PL[i]
                greatest_increase_month = Month_Dates[i]
        if Month_PL[i] < lowest_drop:
                lowest_drop = Month_PL[i]
                lowest_drop_month = Month_Dates[i]
    

#find average
averagelist = (Total_profit_loss/Total_months)

#Print everything

print("Financial Analysis")

print("--------------------------")

print(f'Total Months: {Total_months}')

print(f'Total: ${Total_profit_loss}')

print(f'Average Change: ${averagelist:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {lowest_drop_month} (${lowest_drop})')


#Export to .txt file
text_file = os.path.join('Bank_Analysis.txt')
with open (text_file, "w") as txt_converter:
    txt_converter.write("Financial Analysis\n")

    txt_converter.write("--------------------------\n")

    txt_converter.write(f'Total Months: {Total_months}\n')

    txt_converter.write(f'Total: ${Total_profit_loss}\n')

    txt_converter.write(f'Average Change: ${averagelist:.2f}\n')
    txt_converter.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    txt_converter.write(f'Greatest Decrease in Profits: {lowest_drop_month} (${lowest_drop})\n')
txt_converter.close()