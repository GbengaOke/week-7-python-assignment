import pandas as pd

# Read data from a CSV file
df = pd.read_csv(r'C:\Users\USER\Desktop\iris.data')

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df_cleaned = df.dropna()

# Fill missing values with a specific value
df_filled = df.fillna(0)

# Remove duplicate rows
df_deduplicated = df.drop_duplicates()




