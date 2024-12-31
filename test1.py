import pandas as pd

# Create a sample dataframe
data = {'Name': ['John', 'Bola', 'Ahmed', 'Mary', 'okey', 'Mbanua'],
         'Age': [23, 34,39,25,39,32],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'City': ['Joburg', 'Lagos', 'Accra', 'Cairo', 'Port Harcourt', 'Lome']}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Print dateframe
print(df)