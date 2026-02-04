"""
Title: Car Acceptance Data Visualisation
Author: Shilpa
Course: Data Mining and Machine Learning
University: University of Liverpool

Description:
This script performs exploratory data analysis (EDA) and visualisation
on a car acceptance dataset using Python libraries such as Pandas,
Matplotlib, and Seaborn. The visualisations help identify relationships
between car attributes (price, doors, persons) and acceptance outcomes.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (update the file name if needed)
file_path = 'file_path = 'data/myCarTrainDataset_2024.csv'
file
data = pd.read_csv(file_path)

# Bar Chart: Distribution of Acceptance vs Price
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='price', hue='accept', palette='Set2')
plt.title('Acceptance vs Price', fontsize=16, fontweight='bold')
plt.xlabel('Price', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Acceptance')
plt.show()

# Scatter Plot: Persons vs Doors with Hue by Acceptance
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='doors', y='persons', hue='accept', style='accept', palette='Dark2', s=100)
plt.title('Persons vs Doors by Acceptance', fontsize=16, fontweight='bold')
plt.xlabel('Number of Doors', fontsize=12)
plt.ylabel('Number of Persons', fontsize=12)
plt.legend(title='Acceptance', fontsize=10)
plt.show()

# Histogram: Distribution of Number of Doors
plt.figure(figsize=(8, 6))
sns.histplot(data=data, x='doors', kde=False, bins=5, color='#4c72b0')
plt.title('Distribution of Number of Doors', fontsize=16, fontweight='bold')
plt.xlabel('Number of Doors', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()

# Stacked Bar Chart: Price vs Acceptance
price_accept = pd.crosstab(data['price'], data['accept'])
price_accept.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='coolwarm')
plt.title('Stacked Bar Chart: Price vs Acceptance', fontsize=16, fontweight='bold')
plt.xlabel('Price', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Acceptance')
plt.show()

# Pie Chart: Proportion of Acceptance
accept_counts = data['accept'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(accept_counts, labels=accept_counts.index, autopct='%1.1f%%', startangle=90, colors=['#8dd3c7', 
'#ff7f00'])
plt.title('Proportion of Acceptance', fontsize=16, fontweight='bold')
plt.show()
