import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Food_Production.csv'
df = pd.read_csv(file_path)

# Display the DataFrame
display(df)

# Print the column names
print(df.columns)

# Bar chart for Total Emissions
plt.bar(df['Food product'], df['Total_emissions (KT)'])
plt.xlabel('Food product')
plt.ylabel('Total Emissions (KT)')
plt.title('Total Emissions for Each Food Product')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()

# Set index for the DataFrame
df.set_index('Food product', inplace=True)

# Stacked bar chart for Emissions Breakdown
df[['Animal Feed', 'Farm', 'Processing', 'Transport', 'Packging', 'Retail']].plot(kind='bar', stacked=True)
plt.xlabel('Food product')
plt.ylabel('Emissions Breakdown')
plt.title('Emissions Breakdown for Each Food Product')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()

# Line chart for Eutrophying Emissions
df_no_null = df.dropna(subset=['Eutrophying emissions per 1000kcal', 'Eutrophying emissions per kilogram', 'Eutrophying emissions per 100g protein'])
plt.plot(df_no_null['Food product'], df_no_null['Eutrophying emissions per 1000kcal'], label='per 1000kcal')
plt.plot(df_no_null['Food product'], df_no_null['Eutrophying emissions per kilogram'], label='per kilogram')
plt.plot(df_no_null['Food product'], df_no_null['Eutrophying emissions per 100g protein'], label='per 100g protein')
plt.xlabel('Food product')
plt.ylabel('Eutrophying Emissions')
plt.title('Eutrophying Emissions for Each Food Product')
plt.legend()
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()

# Scatter plot for Freshwater Withdrawals
fig, ax = plt.subplots()
scatter1 = ax.scatter(df['Freshwater withdrawals per 1000kcal '], df['Freshwater withdrawals per kilogram '], label='per kilogram')
scatter2 = ax.scatter(df['Freshwater withdrawals per 1000kcal '], df['Freshwater withdrawals per 100g protein'], label='per 100g protein')
scatter3 = ax.scatter(df['Freshwater withdrawals per kilogram '], df['Freshwater withdrawals per 100g protein'], label='per 1000kcal')

for i, txt in enumerate(df['Food product']):
    ax.annotate(txt, (df['Freshwater withdrawals per 1000kcal '][i], df['Freshwater withdrawals per kilogram '][i]), fontsize=3, textcoords="offset points", xytext=(0,3), ha='center')
    ax.annotate(txt, (df['Freshwater withdrawals per 1000kcal '][i], df['Freshwater withdrawals per 100g protein'][i]), fontsize=3, textcoords="offset points", xytext=(0,3), ha='center')
    ax.annotate(txt, (df['Freshwater withdrawals per kilogram '][i], df['Freshwater withdrawals per 100g protein'][i]), fontsize=3, textcoords="offset points", xytext=(0,3), ha='center')

ax.set_xlabel('Freshwater withdrawals per 1000kcal')
ax.set_ylabel('Freshwater withdrawals')
ax.set_title('Scatter Plot of Freshwater Withdrawals')
ax.legend()
plt.show()

# Grouped bar chart for Land Use
bar_width = 0.25
bar_positions = np.arange(len(df['Food product']))
plt.bar(bar_positions - bar_width, df['Land use per 1000kcal '], width=bar_width, label='per 1000kcal')
plt.bar(bar_positions, df['Land use per kilogram '], width=bar_width, label='per kilogram')
plt.bar(bar_positions + bar_width, df['Land use per 100g protein'], width=bar_width, label='per 100g protein')
plt.xlabel('Food product')
plt.ylabel('Land Use')
plt.title('Grouped Bar Chart for Land Use Comparison')
plt.legend()
plt.xticks(bar_positions, df['Food product'], rotation=45, ha='right')
plt.show()

# Bubble chart for Greenhouse Gas Emissions
fig, ax = plt.subplots()
scatter = ax.scatter(df['Greenhouse gas emissions per 1000kcal '], df['Greenhouse gas emissions per 100g protein '], s=df['Total_emissions (KT)'], alpha=0.7)
for i, txt in enumerate(df['Food product']):
    ax.annotate(txt, (df['Greenhouse gas emissions per 1000kcal '][i], df['Greenhouse gas emissions per 100g protein '][i]), fontsize=3, textcoords="offset points", xytext=(0,3), ha='center')

ax.set_xlabel('Greenhouse Gas Emissions per 1000kcal')
ax.set_ylabel('Greenhouse Gas Emissions per 100g Protein')
ax.set_title('Bubble Chart for Greenhouse Gas Emissions')
ax.grid(True)
plt.show()
#all done
