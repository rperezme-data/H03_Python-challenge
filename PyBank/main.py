## Dependencies
import os
import csv

# Set variable for first month
first_month = True

## Set initial values
month_count = 0
total_pnl = 0
last_pnl = 0
pnl_change_list = []
month_list = []
avg_change = 0


## READ DATA FROM CSV FILE

## Define path for CSV file
input_path = os.path.join('Resources','budget_data.csv')
# print(csv_path)

## Read CSV file
with open(input_path, mode='r', newline='', encoding='utf-8') as csv_file:
    # print(csv_file)
    
    ## Split data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')
    # print(csv_reader)

    ## Get CSV header 
    csv_header = next(csv_reader)
    # print(f"CSV Header: {csv_header}")
    
    ## Loop through CSV rows
    for row in csv_reader:
            # print(row)

            ## Count number of months (rows)
            month_count += 1

            ## Sum Profits/Losses
            total_pnl += float(row[1])

            ## Skip first month since there is no P/L change for the initial value
            if first_month == False:

                ## Compute Profits/Losses change for current month [Change = Current - Last]
                pnl_change_list.append(float(row[1]) - last_pnl)

                ## Store current month in parallel list
                month_list.append(row[0])

            ## Store current P/L for next month's analysis
            last_pnl = float(row[1])

            ## Set variable for subsequent months 
            first_month = False


## Compute P/L average change [AVG = sum(n) / n] 
avg_change = sum(pnl_change_list) / len(pnl_change_list)

## Compute P/L max increase
max_increase_value = max(pnl_change_list)
max_increase_month = month_list[pnl_change_list.index(max_increase_value)]

## Compute P/L max decrease
max_decrease_value = min(pnl_change_list)
max_decrease_month = month_list[pnl_change_list.index(max_decrease_value)]

## Print Report as a function
def print_report():
    return ([
        "Financial Analysis",
        "------------------------------",
        f"Total months: {month_count}",
        f"Total: ${total_pnl:,.0f}",
        f"Average Change: ${avg_change:,.2f}",
        f"Greatest Increase in Profits: {max_increase_month} (${max_increase_value:,.0f})",
        f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease_value:,.0f})"
        ])


## EXPORT REPORT TO A TEXT FILE

## Define path for TXT file
output_path = os.path.join('Analysis','PyBank_Report.txt')
# print(output_path)

## Write TXT file
with open(output_path, mode='w', newline='', encoding='utf-8') as txt_file:
    # print(txt_file)
    for line in print_report():
        txt_file.write(line + "\n")


## PRINT REPORT TO THE TERMINAL
##
for line in print_report():
    print(line)