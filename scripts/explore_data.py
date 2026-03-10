import pandas as pd

# Load the dataset
df = pd.read_csv("data/flipkart_com-ecommerce_sample.csv")

# Preview top rows
print("🔹 Top rows:")
print(df.head(), "\n")

# Dataset shape and column names
print("🔹 Shape:", df.shape)
print("🔹 Columns:", df.columns.tolist(), "\n")

# Check for missing values
print("🔹 Missing values:")
print(df.isnull().sum(), "\n")

# Basic stats
print("🔹 Price Stats:")
print(df[['retail_price', 'discounted_price']].describe())
