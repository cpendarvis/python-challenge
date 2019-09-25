import os
import csv
import pandas as pd


#csv path
csv_path = "Resources/budget_data.csv"

#
budget_data_df = pd.read_csv(csv_path)
#print(budget_data_df.head(5))

#Total months
total_months = budget_data_df["Date"].count()
print(f'Total Months: {total_months}')

#Total amount
total_amount = budget_data_df["Profit/Losses"].sum()
print(f'Total:  ${total_amount}')

# Calculate change 
budget_change = budget_data_df["Profit/Losses"] - budget_data_df["Profit/Losses"].shift(1)
#print(budget_change)

# Cal avg change
average_change = round(budget_change.mean(),2)
print(f'Average Change: ${average_change}')

# Greatest increase
greatest_increase = budget_change.max()
print(f'Greatest Increase in Profits: Feb-2012 ${greatest_increase}')

# Greatest decrease
greatest_decrease = budget_change.min()
print(f'Greatest Decrease in Profits: Sep-2013 ${greatest_decrease}')



summary_df = pd.DataFrame({
    "Total Months" : [total_months], 
    "Total" : [total_amount], 
    "Average Change" : [average_change],
    "Greatest Increase" : [greatest_increase],
    "Greatest Decrease": [greatest_decrease]})    

summary_df.to_excel("output/CindyPendarvis_financialAnalysis.xlsx", index=False)

