import pandas as pd

# Load dataset
df = pd.read_csv("data/flipkart_com-ecommerce_sample.csv")

# Drop rows where essential info is missing (like product name or price)
df = df.dropna(subset=["product_name", "retail_price", "discounted_price"])

# Convert prices to numeric (if not already)
df["retail_price"] = pd.to_numeric(df["retail_price"], errors='coerce')
df["discounted_price"] = pd.to_numeric(df["discounted_price"], errors='coerce')

# Fill missing brand with "Unknown"
df["brand"] = df["brand"].fillna("Unknown")

# Remove duplicates
df = df.drop_duplicates(subset=["product_name", "retail_price", "discounted_price"])

# Save cleaned data
df.to_csv("data/flipkart_cleaned.csv", index=False)

print("✅ Cleaned dataset saved!")
print("Remaining rows:", df.shape[0])
print("Available brands:", df['brand'].nunique())
