import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('tbl_flight_schedules - tbl_flight_schedules.csv')

# Task 3: Data Preparation & Inspection
print("Shape:", df.shape)
print(df.info())
print("Missing Values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

# Task 4: Exploratory Data Analysis
print("\n--- Descriptive Statistics ---")
print(df.describe(include='all'))

# Task 5: Data Visualizations Generation
sns.set_theme(style="whitegrid")

# Chart 1: Top Departure Airports
plt.figure(figsize=(10, 5))
top_dep = df['departure_airport'].value_counts().head(10)
sns.barplot(x=top_dep.index, y=top_dep.values, palette='Blues_d')
plt.title('Top 10 Departure Airports')
plt.savefig('dep_airports.png')
plt.close()

# Chart 2: Top Arrival Airports
plt.figure(figsize=(10, 5))
top_arr = df['arrival_airport'].value_counts().head(10)
sns.barplot(x=top_arr.index, y=top_arr.values, palette='Greens_d')
plt.title('Top 10 Arrival Airports')
plt.savefig('arr_airports.png')
plt.close()

print("All cleaning, EDA, and charts generated successfully!")
