import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Data cleaning
df.dropna(inplace=True)

# Data transformation
df['new_column'] = df['existing_column'] * 2

# Descriptive statistics
print(df.describe())
