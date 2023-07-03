# Imports
import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df = pd.read_excel('Data Set for Task 1.xlsx')

# Pivot the data
## Group the data by 'Subscription Plan Term' and 'Purchase Month', and calculate the sum of 'Transaction Revenue'
grouped_df = df.groupby(['Subscription Plan Term', 'Purchase Month'])['Transaction Revenue'].sum().reset_index()

## Pivot the data to have 'Subscription Plan Term' as columns and 'Purchase Month' as rows
pivot_df = grouped_df.pivot(index='Purchase Month', columns='Subscription Plan Term', values='Transaction Revenue')

## Calculate the total transaction revenue for each subscription plan term
total_revenue = pivot_df.sum()

# Aesthetics
## Sort the columns based on the total revenue in descending order
sorted_columns = total_revenue.sort_values(ascending=False).index

## Reorder the columns in the pivot DataFrame
pivot_df = pivot_df[sorted_columns]

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))

## Plot transaction revenue by subscription plan term
pivot_df.plot(ax=ax)

## Calculate and plot total revenue over time
total_revenue_over_time = pivot_df.sum(axis=1)
total_revenue_over_time.plot(ax=ax, label='Total Revenue', linestyle='--', color='black')

## Set the labels and title
plt.xlabel('Purchase Month')
plt.ylabel('Transaction Revenue')
plt.title('Transaction Revenue by Subscription Plan Term')

## Reorder the legend based on the sorted columns
plt.legend(loc='best', bbox_to_anchor=(1, 1))

## Show the plot
plt.show()