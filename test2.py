import pandas as pd

# Read data from a CSV file
df = pd.read_csv(r'C:\Users\USER\Desktop\iris.data')

# Display the first few rows of the DataFrame
print(df.head())

# Display basic information about the dataset
print(df.info())

# Display statistical summary of the dataset
print(df.describe())

# Display column names
print(df.columns)

# Display the shape of the dataset (rows, columns)
print(df.shape)
